"""project_django URL Configuration

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
from django.contrib import admin
from django.urls import  path
from annuaire.views import listParticulier
from annuaire.views import listEntreprise
from annuaire.views import detailContact
from annuaire.views import listContacts
from project_django.views import addition

from project_django.views import helloWorld

urlpatterns = [
        path('admin/', admin.site.urls),
        path('',helloWorld, name ="acceuil"),
        path('addition/',addition,name='addition'),
        path('annuaire/',listContacts,name="list-contact"),
        path('annuaire/particuliers/',listParticulier,name="list-particulier"),
        path('annuaire/entreprise/',listEntreprise,name="list-entreprise"),
        path('annuaire/detail-contact/',detailContact,name='detail-contact')
      
    
]
