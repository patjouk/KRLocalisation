from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Restaurant(models.Model):
    num_entree = models.Field.primary_key(primary_key=True)
    nom = models.CharField()
    nom_coreen = models.CharField()
    latitude = models.BigIntergerField()
    longitude = models.BigIntergerField()
    code_postal = models.SmallIntergerField()
    adresse = models.CharField()
    num_tel = models.SmallIntergerField()
    num_siret = models.BigIntergerField()
    proprietaire = models.CharField()
    proprietaire_coreen = models.CharField()
    date_immatriculation = models.DateField()
    date_radiation = models.DateField()
    site_web = models.URLField()
    statut_societe = models.CharField()
    contact = models.BooleanField()
    interview = models.BooleanField()
    annuaire_alloparis = models.BooleanField()
    annuaire_hansik = models.BooleanField()
    radiation = models.BooleanField()
    nolebang = models.BooleanField()
    notes = models.TextField()

    def __str__(self):
        return self.nom