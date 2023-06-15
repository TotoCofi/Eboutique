import json
from urllib import request
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

def add_acheter(request):
    pro_id= request.POST.get('pro_id')
    cli_id= request.POST.get('cli_id')
    qte= int(request.POST.get('qte'))
 
    commande_id= request.POST.get('commande_id')
    produit =Produits.objects.filter(id=pro_id).first()
    client =Clients.objects.filter(id=cli_id).first()
    


    commande =Commandes.objects.filter(id=commande_id).first()

    if not commande:
       if client:
          user=request.user
          commande =Commandes(client=client,user=user)    
          commande.save()
    if produit and client:
        produit.quantite-=qte
        produit.save()
        prixcommande=int(qte * produit.prix)
        acheter=Acheter(commande=commande,Produit=produit,quantite=qte,prixcommande=prixcommande)
        acheter.save()
        achat = Acheter.objects.filter(commande=commande).select_related('Produit').values('quantite', 'prixcommande','Produit__nom', 'Produit__prix','id')
        serialized_achat = json.dumps(list(achat))

        return JsonResponse({'commande_id': commande.id, 'acheter': serialized_achat}, safe=False)
    else:  
       return JsonResponse({'produit':'prix unitaire'})   

def del_acheter(request):
    id= request.POST.get('id')
    acheter =Acheter.objects.filter(id=id).first()
    qte= int(request.POST.get('qte'))
    produit=Produits.objects.filter(id=acheter.Produit_id).first()
    if acheter:
        prix= acheter.prixcommande
        if acheter.delete():
            produit.quantite+=qte
            produit.save()
            produit_data = {'nom': produit.nom, 'id': produit.id}
            return JsonResponse({'resp':'true','produit':produit_data,'prix':prix}, safe=False)
        
    return JsonResponse({'resp':'false'}) 
def valid_achat(request):
    commande_id= request.POST.get('commande_id')
    mode_id= request.POST.get('mode')
    total= request.POST.get('total')
    commande =Commandes.objects.filter(id=commande_id).first()
    mode =Mode_payements.objects.filter(id=mode_id).first()
    user=request.user
    if commande:
        commande.prixtotal=total
        payement=Payements(commande=commande ,mode_payement=mode,user=user)
        payement.save()
        commande.save()
        return JsonResponse({'resp':'true'}) 
    return JsonResponse({'resp':'false'}) 

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
#@login_required
def user(request):
    rol= Roles.objects.all()
    users=Users.objects.select_related('role')
    if request.method == 'POST':
    
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
def client(request): 
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

def categorie(request):
    categories = Categories.objects.all() # on recupère tout les catégorie enregistrés dans la base de données
    if request.method == "POST":
        nom = request.POST['nom']
        user = Users.objects.get(id = request.user.id)  # user reprsente un instance de la clase Users
        categorie = Categories(nom = nom,user = user)
        categorie.save()
    return render(request,'categorie.html',{'categories':categories})

def produit(request):
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

def update_client(request,id):
    client_u = get_object_or_404(Clients, pk = id)
    if request.method == "POST":
        client_u.nom = request.POST['nom']
        client_u.adresse = request.POST["adresse"]
        client_u.phone = request.POST["phone"]
        client_u.user = Users.objects.get(id = request.user.id)
        client_u.save()
        return redirect('client')

    return render(request,'update_client.html',{'clients_u':client_u})
def update_user(request,id):
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
            user.save()
            return redirect('user')

    return render(request,'update_user.html',{'user':user,'roles':rol})

def update_categorie(request,id):
    categorie_u = get_object_or_404(Categories, pk = id)
    if request.method == "POST":
        categorie_u.nom = request.POST['nom']
        categorie_u.user = Users.objects.get(id = request.user.id)
        categorie_u.save()
        return redirect('categorie')

    return render(request,'update_categorie.html',{'categories_u':categorie_u})
 

def update_produit(request,id):
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
 
def delete_client(request,id):
    client_d = get_object_or_404(Clients, pk = id)
    client_d.delete()
    return redirect('client')


def delete_categorie(request,id):
    categorie_d = get_object_or_404(Categories, pk = id)
    categorie_d.delete()
    return redirect('categorie')

def delete_produit(request,id):
    produit_d = get_object_or_404(Produits, pk = id)
    produit_d.delete()
    return redirect('produit')

def add_commande(request):
    clients = Clients.objects.all()
    produits = Produits.objects.all()
    Modes=Mode_payements.objects.all()
    return render(request,'Ajout_commande.html',{'cli':clients,'pros':produits,"modes":Modes})
@login_required
def commande(request):
    commande = Commandes.objects.filter(prixtotal__gt=0).select_related('client','user')
    return render(request,'commande.html',{'commandes':commande})
@login_required
def payement(request):
    payement= Payements.objects.select_related('commande__client','user')
    return render(request,'payement.html',{'payements':payement})
@login_required
def facture(request):
    return render(request,'facture.html')

def detaille_commande(request,id):
    cmd_id = get_object_or_404(Commandes,pk = id)
    acheter = Acheter.objects.filter(commande = cmd_id).select_related('Produit')
    
    return render(request,'detaille_commande.html',{'det_cmd':acheter,'cmd_cli':cmd_id})