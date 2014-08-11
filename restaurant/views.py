from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Restaurant
from .tables import TableauRestaurant

def tableau_donnees(request):
        tabrestaurants = TableauRestaurant(Restaurant.objects.order_by('nom').all())
        RequestConfig(request, paginate={"per_page":150}).configure(tabrestaurants)
        return render(request, 'restaurant/tableau_donnees.html', {"restaurants": tabrestaurants})
