from django.db import models
from django.db.models import F
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class Users(AbstractUser):
    phone = models.CharField(max_length=50, unique=True, null=True)
    password=models.TextField()
    role = models.ForeignKey('Roles', on_delete=models.CASCADE)

class Roles(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    created_at =models.DateTimeField(default=timezone.now)
    
class Categories(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    user= models.ForeignKey('Users', on_delete=models.CASCADE)
    created_at =models.DateTimeField(default=timezone.now)
    categorie = models.ForeignKey("self", null=True, blank= True,on_delete=models.CASCADE)

    def get_sous_cat(id):#récupérer les sous-catégories d'une catégorie spécifique :
        return Categories.objects.filter(categorie_id =id)
    
    def has_sous_cat(self):# pour vérifier si une catégorie a des sous-catégories :
        return Categories.objects.filter(categorie = self)
    

class Produits(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    description =models.TextField()
    prix=models.IntegerField(default=0)
    quantite=models.IntegerField(default=0)
    seuil=models.IntegerField(default=0)
    user= models.ForeignKey('Users', on_delete=models.CASCADE)
    categorie = models.ForeignKey('Categories', on_delete=models.CASCADE)
    created_at =models.DateTimeField(default=timezone.now)

class Clients(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    adresse = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, unique=True, null=True)
    user= models.ForeignKey('Users', on_delete=models.CASCADE)
    created_at =models.DateTimeField(default=timezone.now)

class Commandes(models.Model):
    prixtotal=models.IntegerField(default=0)
    client= models.ForeignKey('Clients', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    user= models.ForeignKey('Users', on_delete=models.CASCADE)
    created_at =models.DateTimeField(default=timezone.now)

class Acheter(models.Model):
    commande= models.ForeignKey('Commandes', on_delete=models.CASCADE)
    Produit= models.ForeignKey('Produits', on_delete=models.CASCADE)
    quantite=models.IntegerField(default=0)
    prixcommande=models.IntegerField(default=0)

class Mode_payements(models.Model):
    mode = models.CharField(max_length=255, unique=True)
    user= models.ForeignKey('Users', on_delete=models.CASCADE)
     
class Payements(models.Model):
    commande= models.ForeignKey('Commandes', on_delete=models.CASCADE)
    mode_payement= models.ForeignKey('Mode_payements', on_delete=models.CASCADE)
    user= models.ForeignKey('Users', on_delete=models.CASCADE)
    created_at =models.DateTimeField(default=timezone.now)
 

class Log(models.Model):
    
    user= models.ForeignKey('Users', on_delete=models.CASCADE)
    message=models.TextField()
    type= models.CharField(max_length=255,default=None)
    created_at =models.DateTimeField(default=timezone.now)
    

