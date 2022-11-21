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
liste=[]
def listContacts(request):
   liste = Contact.objects.all()
   print(liste)
   return render (request,'list.html',{'contacts':liste})
  
def detailContact(request):
  global contacts
  for i in contacts :
   if i["nom"]== request.GET.get('nom'):
        
    return render (request,'contact.html',{'identiter':i})
    

# def detailContact(request,nom):
#   contact =Contact.objects.get(nom=nom)
#   liste1= Contact.objects.all()

#   for i in liste1:
#       if i["nom"]== contact :
#        return render (request,'contact.html',{'identiter':i}) 