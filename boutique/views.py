from django.shortcuts import render
from .models import Roles,Users
# Create your views here.

def acceuil(request):
    return render(request,'index.html')

def user(request):
    rol= Roles.objects.all()
    if request.method == 'POST':
    
       email=request.POST.get('email')
       user = Users.objects.filter(email=email).first()
       if user:
         message = "Email existe déja"
         return render(request, 'user.html',{'error_messages': message})
       else : 
            nom= request.POST.get('nom')
            prenom= request.POST.get('prenom')
            password= request.POST.get('password')
            c_password = request.POST.get('c_password')
            if len(password)<8:
                message = "Le mot de passe doit contenir au moins 8 caractères."
                return render(request, 'user.html',{'error_messages': message})
                    
            if password != c_password :  
                message = "Les mot de passe doivent etre identique"
                return render(request, 'user.html',{'error_messages': message})
            

    
    return render(request,'user.html',{'roles':rol})

def client(request):
    return render(request,'client.html')

def categorie(request):
    return render(request,'categorie.html')

def produit(request):
    return render(request,'produit.html')

def commande(request):
    return render(request,'commande.html')

def payement(request):
    return render(request,'payement.html')

def facture(request):
    return render(request,'facture.html')