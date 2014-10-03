from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.gis.db import models
import django_filters

class Restaurant(models.Model):
    num_entree = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    nom_coreen = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    code_postal = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    num_tel = models.CharField(max_length=100)
    num_siret = models.CharField(max_length=100)
    proprietaire = models.CharField(max_length=100)
    proprietaire_coreen = models.CharField(max_length=100)
    date_immatriculation = models.DateField(blank=True, null=True)
    date_radiation = models.DateField(blank=True, null=True)
    site_web = models.URLField()
    statut_societe = models.CharField(max_length=100)
    contact = models.BooleanField(default=False)
    interview = models.BooleanField(default=False)
    annuaire_alloparis = models.BooleanField(default=False)
    annuaire_hansik = models.BooleanField(default=False)
    radiation = models.BooleanField(default=False)
    nolebang = models.BooleanField(default=False)
    notes = models.TextField()
    geom = models.PointField(blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return self.nom

