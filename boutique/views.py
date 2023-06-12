from nis import cat
from pydoc import cli
from django.http import JsonResponse
from django.shortcuts import redirect, render
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
            password = request.POST.get('password')
            remember_me = request.POST.get('remember_me')
            user= Users.objects.filter(email=email).first()
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
                        user = authenticate(request,email=email, password=password)
                        if user is not None:
                            login(request, user)  
                            return redirect('/')
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
                return render(request, 'user.html',{'error_messages': message})
               
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
                    user = Users.objects.create_superuser(username = email, is_active=0, first_name = nom ,last_name = prenom ,phone=phone,email = email,role=role)
                    user.set_password(password) 
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
    clients = Clients.objects.all()
    if request.method == "POST":
        nom = request.POST['nom']
        adresse = request.POST['adresse']
        phone = request.POST['phone']
        user = Users.objects.get(id = request.user.id )
        client = Clients(nom = nom,adresse = adresse,phone = phone,user = user ) 
        client.save()
    return render(request,'client.html',{'clients':clients})

def categorie(request):
    categories = Categories.objects.all()
    if request.method == "POST":
        nom = request.POST['nom']
        user = Users.objects.get(id = request.user.id)
        categorie = Categories(nom = nom,user = user)
        categorie.save()
    return render(request,'categorie.html',{'categories':categories})

def produit(request):
    produits = Produits.objects.all()
    categories = Categories.objects.all()
    if request.method == "POST":
        nom = request.POST['nom']
        description = request.POST['description']
        prix = request.POST['prix']
        quantiter = request.POST['quantiter']
        seuil = request.POST['seuil']
        id = request.POST['cate']
        cat = Categories.objects.get(id = id )
        user = Users.objects.get(id = request.user.id)
        produit = Produits(nom = nom,description = description,prix = prix,quantite = quantiter,seuil = seuil,categorie = cat,user = user)
        produit.save()
    return render(request,'produit.html',{"categories":categories,"produits":produits})

def commande(request):
    return render(request,'commande.html')
@login_required
def payement(request):
    return render(request,'payement.html')
@login_required
def facture(request):
    return render(request,'facture.html')