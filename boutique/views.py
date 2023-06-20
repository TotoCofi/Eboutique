import json
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render ,get_object_or_404
from .models import *
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib.auth import logout,authenticate, login
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
import re
import random
import string
from django.core import serializers
@login_required
def permission(request,type):
    user=Users.objects.select_related('role').get(id=request.user.id)
    if user.role.nom =='Admin':
        return True
    elif type=='caisse' and user.role.nom=="Caissier":
    
        return True
    elif type=='gerant' and user.role.nom=="Gerant":
        
        return True
    
    else:
        return False

@login_required
def prix_unitaire(request):
    pro_id= request.POST.get('id')
    produit =Produits.objects.filter(id=pro_id).first()
    if produit:
     return JsonResponse({'produit':produit.prix,"qte":produit.quantite})
    else:  
     return JsonResponse({'produit':'prix unitaire'})   

def verification(request):
  if request.method == 'POST':
      code = request.POST.get('code')
      email = request.session.get('email')
      vcode = request.session.get('code')
      if email is not None:
          user= Users.objects.filter(email=email).first()
          if user is not None:
              if vcode == code:
                user.is_active=1
                user.save()
                login(request, user)  
                return redirect('/')

              else:
                message = " code non valide"
                return render(request, 'verification.html',{'error_messages': message})
            
          else:
                return redirect('login')
      else:
         message = " delai expiré"
         return render(request, 'verification.html',{'error_messages': message})
  else:
    return render(request, 'verification.html')

def generate_unique_code():
    length = 6  # Longueur du code à usage unique
    characters = string.ascii_letters + string.digits  # Caractères autorisés pour le code
    code = ''.join(random.choices(characters, k=length))
    return code

def codemail(request,code,email):
            subject = "Votre code à usage unique"
            from_email = "noreply@example.com"
            to_email = email  # Remplacer par l'e-mail de l'utilisateur enregistré
            message = render_to_string('code-mail.html', {'email': email, 'code': code})
                                            
            send_mail(subject, strip_tags(message), from_email, [to_email], html_message=message)
       
            request.session['email']=email
            request.session['code']=code
            durée_expiration = timedelta(hours=2)  # Durée d'expiration de 2 heures
            request.session.set_expiry(durée_expiration.total_seconds())

def acceuil(request):
    if not request.user.id:
        if request.method == 'POST':
            email = request.POST.get('email')
            print(email)
            password = request.POST.get('password')
            print(password)
            remember_me = request.POST.get('remember_me')
            user= Users.objects.filter(email=email).first()
            print(user)
            if user is not None:
                    if user.is_staff == 0:
                       messages.error(request,'Votre Compte est désactivé')
                    else:
                        if user.is_active==0:
                            if user.check_password(password):
                            
                    
                                code = generate_unique_code()
                                user.code=code
                                
                                codemail(request,code,user.email)
                            
                                return redirect('verification')

                            else:
                                message = "Email ou mot de passe non valide"
                                return render(request, 'login.html',{'error_messages': message})
                        else:
                                #user = authenticate(request,email=email, password=password)
                                print(user)
                                if user is not None:
                                    if user.check_password(password):
                                        login(request, user)  
                                        return redirect('/')
                                    else:
                                        message = "Mot de passe non valide"
                                    return render(request, 'login.html',{'error_messages': message})
                                else:
                                    message = "Email ou mot de passe non valide"
                                    return render(request, 'login.html',{'error_messages': message,} )
                        
            else:
                    message = "Email  non valide"
                    return render(request, 'login.html',{'error_messages': message,})

        return render(request,'login.html')
    else:
       return render(request,'index.html')

def user_logout(request):
  logout(request)
  return redirect('/')

@login_required
def user(request):
   if permission(request,'admin')== True: 
    rol= Roles.objects.all()
    users=Users.objects.select_related('role')
    if request.method == 'POST':
        if 'mdp' in request.POST:
            user=Users.objects.filter(id=request.POST['id']).first()
            if request.POST['mdp'] == request.POST['c_mdp']:
                user.set_password(request.POST['mdp'])
                user.save()
                messages.success(request,'Le mot de passe à été modifier avec succes')
            else:
                messages.error(request,'Les mots de passe ne sont pas identique')
        else: 
            email=request.POST.get('email')
            user = Users.objects.filter(email=email).first()
            if user:
                message = "Email existe déja"
                return render(request, 'user.html',{'error_messages': message})
       
            else : 
                benin_regex = r"^(\+229)?\d{8}$"
                phone=request.POST.get('phone')

            if not re.match(benin_regex, phone):
                message = "Numéro de téléphone invalide ou non du Bénin"
                return render(request, 'user.html',{'roles':rol,'error_messages': message,'users':users})
               
            nom= request.POST.get('nom')
            prenom= request.POST.get('prenom')
            roll= request.POST.get('role')
            password= request.POST.get('password')
            c_password = request.POST.get('c_password')
            role=Roles.objects.get(id=roll)
            if role:
            
                if len(password)<8:
                    message = "Le mot de passe doit contenir au moins 8 caractères."
                    return render(request, 'user.html',{'roles':rol,'error_messages': message,'users':users})
                        
                if password != c_password :  
                    message = "Les mot de passe doivent etre identique"
                    return render(request, 'user.html',{'roles':rol,'error_messages': message,'users':users})
                else:
                    user = Users.objects.create_superuser(password=password, username = email, is_active=0, first_name = nom ,last_name = prenom ,phone=phone,email = email,role=role)
                    #user.set_password(password) 
                    subject = 'Bienvenue !'
                     
                    from_email = 'your_email@example.com'
                    recipient_list = [email]
                    message = render_to_string('register-mail.html', {'email': email, 'password': password})
                                            
                    send_mail(subject, strip_tags(message), from_email, recipient_list, html_message=message)

                    user.save()
                    users=Users.objects.select_related('role')
                    message = "Utilisateur enregister"
                    return render(request, 'user.html',{'roles':rol,'messages': message,'users':users})
            else:
                
                    message = "role innexistant"
                    return render(request, 'user.html',{'roles':rol,'error_messages': message,'users':users})
    return render(request,'user.html',{'roles':rol,'users':users})
   else:
       return render(request,'401.html')
       
@login_required
def client(request):
   if permission(request,'caisse')== True: 
    clients = Clients.objects.all() # on recupère tout les clients enregistrés dans la base de données
    if request.method == "POST":
        nom = request.POST['nom']
        adresse = request.POST['adresse']
        phone = request.POST['phone']
        user = Users.objects.get(id = request.user.id )# user reprsente un instance de la clase Users
        cli = Clients.objects.filter(phone = phone).first() # Verifions si le numero exist
        if cli:
                messages.error(request,'le numéro existe déja')
        else:
            client = Clients(nom = nom,adresse = adresse,phone = phone,user = user ) 
            client.save()
    return render(request,'client.html',{'clients':clients})
   else:
       return render(request,'401.html')   

@login_required
def categorie(request):
   if permission(request,'gerant')== True: 
    categories = Categories.objects.all() # on recupère tout les catégorie enregistrés dans la base de données
    if request.method == "POST":
        nom = request.POST['nom']
        user = Users.objects.get(id = request.user.id)  # user reprsente un instance de la clase Users
        categorie = Categories(nom = nom,user = user)
        categorie.save()
    return render(request,'categorie.html',{'categories':categories})
   else:
       return render(request,'401.html')  

@login_required
def produit(request):
   if permission(request,'gerant')== True: 
    produits = Produits.objects.all() # on recupère tout les produits enregistrés dans la base de données
    categories = Categories.objects.all()
    if request.method == "POST":
        nom = request.POST['nom']
        description = request.POST['description']
        prix = request.POST['prix']
        quantiter = request.POST['quantiter']
        seuil = request.POST['seuil']
        id = request.POST['cate']
        cat = Categories.objects.get(id = id )  # cat reprsente un instance de la clase Catégories
        user = Users.objects.get(id = request.user.id)  # user reprsente un instance de la clase Users
        pro = Produits.objects.filter(nom = nom) # verifions si le produit exist dans la base de donnée
        if pro: 
            messages.error(request,'Ce produit existe déja')
        else:
            produit = Produits(nom = nom,description = description,prix = prix,quantite = quantiter,seuil = seuil,categorie = cat,user = user)
            produit.save()
    return render(request,'produit.html',{"categories":categories,"produits":produits})
   else:
       return render(request,'401.html')  

@login_required
def update_client(request,id):
   if permission(request,"caisse")== True:   
    client_u = get_object_or_404(Clients, pk = id)
    if request.method == "POST":
        client_u.nom = request.POST['nom']
        client_u.adresse = request.POST["adresse"]
        client_u.phone = request.POST["phone"]
        client_u.user = Users.objects.get(id = request.user.id)
        client_u.save()
        return redirect('client')

    return render(request,'update_client.html',{'clients_u':client_u})
   else:
       return render(request,'401.html')

@login_required
def update_user(request,id):
   if permission(request,'admin')== True: 
    rol= Roles.objects.all()
    user = get_object_or_404(Users, pk = id)
    if request.method == "POST":
            benin_regex = r"^(\+229)?\d{8}$"
            phone=request.POST.get('phone')

            if not re.match(benin_regex, phone):
                message = "Numéro de téléphone invalide ou non du Bénin"
                return render(request, 'update_user.html',{'error_messages': message,'user':user,'roles':rol})
            user.first_name = request.POST['nom']
            user.first_prenom = request.POST['prenom']
            user.role_id= request.POST.get('role')
            user.email = request.POST["email"]
            user.phone = request.POST["phone"]
            user.is_staff= request.POST['statut']
            user.save()
            return redirect('user')

    return render(request,'update_user.html',{'user':user,'roles':rol})
   else:
       return render(request,'401.html')  

@login_required
def update_categorie(request,id):
   if permission(request,'gerant')== True: 
    categorie_u = get_object_or_404(Categories, pk = id)
    if request.method == "POST":
        categorie_u.nom = request.POST['nom']
        categorie_u.user = Users.objects.get(id = request.user.id)
        categorie_u.save()
        return redirect('categorie')

    return render(request,'update_categorie.html',{'categories_u':categorie_u})
   else:
       return render(request,'401.html')  
 
@login_required
def update_produit(request,id):
   if permission(request,'gerant')== True: 
    produit_u = get_object_or_404(Produits, pk = id)
    if request.method == "POST":
        produit_u.nom = request.POST['nom']
        produit_u.description = request.POST['description']
        produit_u.prix = request.POST['prix']
        produit_u.quantite = request.POST['quantite']
        produit_u.seuil = request.POST['seuil']
        produit_u.user = Users.objects.get(id = request.user.id)
        produit_u.save()
        return redirect('produit')

    return render(request,'update_produit.html',{'produits_u':produit_u})
   else:
       return render(request,'401.html')   

@login_required
def delete_client(request,id):
   if permission(request,'caisse')== True: 
    client_d = get_object_or_404(Clients, pk = id)
    client_d.delete()
    return redirect('client')
   else:
       return render(request,'401.html')   

@login_required
def delete_categorie(request,id):
   if permission(request,'gerant')== True: 
    categorie_d = get_object_or_404(Categories, pk = id)
    categorie_d.delete()
    return redirect('categorie')
   else:
       return render(request,'401.html')   

@login_required
def delete_produit(request,id):
   if permission(request,'gerant')== True: 
    produit_d = get_object_or_404(Produits, pk = id)
    produit_d.delete()
    return redirect('produit')
   else:
       return render(request,'401.html')   

@login_required
def add_commande(request):
   if permission(request,'caisse')== True:  
    clients = Clients.objects.all()
    produits = Produits.objects.filter(quantite__gt=0).all()
    Modes=Mode_payements.objects.all()
    if request.method == "POST":
        cli_id= request.POST.get('client')
        total=request.POST.get('total')
        client =get_object_or_404(Clients,pk =cli_id)
        pro_id= request.POST.getlist('produit')
        qte= request.POST.getlist('qte_commande')
        prix= request.POST.getlist('prixtotal')
        taille_liste = len( pro_id)
        mode_id= request.POST.get('mode')
        user=request.user
        mode =get_object_or_404(Mode_payements,pk =mode_id)
        if taille_liste!=0:   

            if client:
                 if mode:
                    commande =Commandes(client=client,user=user,prixtotal=total)
                    commande.save()
                    payement=Payements(commande=commande ,mode_payement=mode,user=user)
                    payement.save()   
                 else:
             
                    message = "Erreur de mode de payement"
                        
                    return render(request,'Ajout_commande.html',{'error_messages': message,'cli':clients,'pros':produits,"modes":Modes})    
            
            else:
               message = "Client introuvable"
               return render(request,'Ajout_commande.html',{'error_messages': message,'cli':clients,'pros':produits,"modes":Modes})


            for i in range(taille_liste):
                
                produit =Produits.objects.filter(id=pro_id[i]).first()
                if produit:
                        produit.quantite-= int(qte[i])
                        produit.save()
                        prixcommande=prix[i]
                        acheter=Acheter(commande=commande,Produit=produit,quantite=qte[i],prixcommande=prixcommande)
                        acheter.save() 
            message = "Commande ajouter"
            return render(request,'Ajout_commande.html',{'messages': message,'cli':clients,'pros':produits,"modes":Modes})

    return render(request,'Ajout_commande.html',{'cli':clients,'pros':produits,"modes":Modes})
   
   
   
   else:
       return render(request,'401.html')  

@login_required
def commande(request):
   if permission(request,'caisse')== True:   
    commande = Commandes.objects.select_related('client','user')
    return render(request,'commande.html',{'commandes':commande})
   else:
       return render(request,'401.html') 

@login_required
def payement(request):
   if permission(request,'caisse')== True:    
    payement= Payements.objects.select_related('commande__client','user')
    return render(request,'payement.html',{'payements':payement})
   else:
       return render(request,'401.html')

@login_required
def detaille_commande(request,id):
   if permission(request,'caisse')== True: 
    cmd_id = get_object_or_404(Commandes,pk = id)
    acheter = Acheter.objects.filter(commande = cmd_id).select_related('Produit')
    
    return render(request,'detaille_commande.html',{'det_cmd':acheter,'cmd_cli':cmd_id})
   else:
       return render(request,'401.html')   

def detaille_payement(request,id_pay):
   if permission(request,'caisse')== True: 
    payement = Payements.objects.get(id = id_pay)
    return render(request,'detaille_payement.html',{'payements':payement})
   else:
       return render(request,'401.html')   
   

def setting(request):
    user = get_object_or_404(Users, pk=request.user.id)
    
    if request.method == 'POST':
        a_mdp = request.POST['a_mdp']
        n_mpd = request.POST['n_mdp']
        c_mpd = request.POST['c_mdp']
        
        if user.check_password(a_mdp):
            if n_mpd == c_mpd:
                user.set_password(n_mpd)
                user.save()
                messages.success(request, 'Le mot de passe a été modifié avec succès')
                logout(request)
                return redirect('/')
            else:
                messages.error(request, 'Le nouveau mot de passe et la confirmation ne correspondent pas')
        else:
            messages.error(request, 'L\'ancien mot de passe ne correspond pas')
    
    return render(request, 'setting.html')
