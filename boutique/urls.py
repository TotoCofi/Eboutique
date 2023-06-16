"""Eboutique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pydoc import cli
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from boutique.views import *




urlpatterns = [
    path('verification', verification, name='verification'),
    path('admin/', admin.site.urls),
    path('',acceuil,name="acceuil"),  
    path('logout',user_logout,name="logout"),
    path("user",user,name="user"),
    path('client',client,name='client'),
    path('categorie',categorie,name="categorie"),
    path('produit',produit,name="produit"),
    path('commande',commande,name='commande'),
    path('add_commande',add_commande,name='add_commande'),
    path('prix_unitaire/',prix_unitaire,name='prix_unitaire/'),
    path('add_acheter/',add_acheter,name='add_acheter/'),
    path('del_acheter/',del_acheter,name='del_acheter/'),
    path('valid_achat/',valid_achat,name='valid_achat/'),
    path('payement',payement,name='payement'),
    path('facture',facture,name='facture'),
    path('update_client/<int:id>',update_client,name='update_client'),
    path('update_user/<int:id>',update_user,name='update_user'),
    path('update_categorie/<int:id>',update_categorie,name='update_categorie'),
    path('update_produit/<int:id>',update_produit,name='update_produit'),
    path('delete_client/<int:id>',delete_client,name='delete_client'),
    path('delete_categorie/<int:id>',delete_categorie,name='delete_categorie'),
    path('delete_produit/<int:id>',delete_produit,name='delete_produit'),
    path('det_commande/<int:id>',detaille_commande,name='det_commande'),
    path('detaille_payement/<int:id_pay>',detaille_payement,name='detaille_payement')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)