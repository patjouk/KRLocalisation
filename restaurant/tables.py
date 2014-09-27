import django_filters
import django_tables2 as tables
from .models import Restaurant

class TableauRestaurant(tables.Table):
    class Meta:
        model = Restaurant
        exclude = ('num_entree', 'latitude', 'longitude', 'geom')
        attrs = {"class": "paleblue"}

class FiltreRestaurant(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = ['code_postal', 'statut_societe', 'contact', 'interview', 'annuaire_alloparis', 'annuaire_hansik', 'radiation', 'nolebang']
