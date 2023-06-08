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
    path('admin/', admin.site.urls),
    path('',acceuil,name="acceuil"),
    path("user",user,name="user"),
    path('client',client,name='client'),
    path('categorie',categorie,name="categorie"),
    path('produit',produit,name="produit"),
    path('commande',commande,name='commande'),
    path('payement',payement,name='payement'),
    path('facture',facture,name='facture'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)