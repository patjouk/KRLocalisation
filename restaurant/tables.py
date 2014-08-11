import django_tables2 as tables
from .models import Restaurant

class TableauRestaurant(tables.Table):
    class Meta:
        model = Restaurant
        fields = ('nom', 'nom_coreen', 'code_postal', 'adresse', 'num_tel', 'num_siret', 'proprietaire', 'proprietaire_coreen', 'date_immatriculation', 'date_radiation', 'site_web', 'statut_societe', 'contact', 'interview', 'annuaire_alloparis', 'annuaire_hansik', 'radiation', 'nolebang', 'notes')