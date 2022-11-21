from django.shortcuts import render
from annuaire.models import Contact

# Create your views here.

contacts = [
       {
          "nom": "Cassidy",
          "prenom": "Hammond",
          "telephone": "03 94 96 50 97"
        },
        {
          "nom": "Charde",
          "prenom": "Hyde",
          "telephone": "03 44 84 02 60"
        },
        {
          "nom": "Dorian",
          "prenom": "Bailey",
          "telephone": "03 78 24 49 97"
        },
        {
          "nom": "Vivien",
          "prenom": "Duffy",
          "telephone": "03 26 81 80 44"
        },
        {
          "nom": "Ivory",
          "prenom": "Colon",
          "telephone": "03 85 87 65 55"
        }
    ]


def listContacts(request):
   liste = Contact.objects.all()
   return render (request,'list.html',{'contacts':liste})

  
def detailContact(request):
  nomValider =request.GET.get('nom')
  contacts=Contact.objects.filter(nom=nomValider).values() 
  for contact in contacts:
    return render (request,'contact.html',{'identiter':contact}) 

