from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Restaurant
from .tables import TableauRestaurant, FiltreRestaurant

def tableau_donnees(request):
        tabrestaurants = TableauRestaurant(Restaurant.objects.order_by('nom').all())
        RequestConfig(request, paginate={"per_page":200}).configure(tabrestaurants)
        return render(request, 'restaurant/tableau_donnees.html', {"restaurants": tabrestaurants})

def cartographie_simple(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/cartographie.html', {"restaurants": restaurants})

def list_restaurant(request):
    f = FiltreRestaurant(request.GET, queryset=Restaurant.objects.all())
    return render(request, 'restaurant/tableau_donnees_trie.html', {'filtre': f})