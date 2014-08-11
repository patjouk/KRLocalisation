import django_tables2 as tables
from .models import Restaurant

class TableauRestaurant(tables.Table):
    class Meta:
        model = Restaurant
        exclude = ('num_entree', 'latitude', 'longitude')
        attrs = {"class": "paleblue"}