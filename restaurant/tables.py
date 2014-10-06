import django_filters
import django_tables2 as tables
from .models import Restaurant
from django_tables2.utils import A

class TableauRestaurant(tables.Table):
    nom = tables.LinkColumn('detail', args=[A('pk')])

    class Meta:
        model = Restaurant
        exclude = ('num_entree', 'latitude', 'longitude', 'geom', 'num_siret', 'proprietaire', 'proprietaire_coreen', 'statut_societe', 'annuaire_alloparis', 'annuaire_hansik', 'nolebang', 'notes', 'site_web')
        attrs = {"class": "paleblue"}

class FiltreRestaurant(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = ['code_postal', 'radiation', 'contact', 'interview']
