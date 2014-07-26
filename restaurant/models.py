from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Restaurant(models.Model):
    num_entree = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    nom_coreen = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    code_postal = models.SmallIntegerField()
    adresse = models.CharField(max_length=100)
    num_tel = models.CharField(max_length=100)
    num_siret = models.CharField(max_length=100)
    proprietaire = models.CharField(max_length=100)
    proprietaire_coreen = models.CharField(max_length=100)
    date_immatriculation = models.DateField()
    date_radiation = models.DateField()
    site_web = models.URLField()
    statut_societe = models.CharField(max_length=100)
    contact = models.BooleanField()
    interview = models.BooleanField()
    annuaire_alloparis = models.BooleanField()
    annuaire_hansik = models.BooleanField()
    radiation = models.BooleanField()
    nolebang = models.BooleanField()
    notes = models.TextField()

    def __str__(self):
        return self.nom