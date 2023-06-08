from django.shortcuts import render

# Create your views here.

def acceuil(request):
    return render(request,'index.html')

def user(request):
    return render(request,'user.html')

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