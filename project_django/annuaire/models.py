from django.db import models

# Create your models here.

class Contact (models.Model):
    nom = models.CharField(max_length=256, blank=False)
    prenom = models.CharField(max_length=128, blank=True)
    telephone =models.CharField(max_length=128, blank=True)
    entreprise = models.BigIntegerField(default=False)
