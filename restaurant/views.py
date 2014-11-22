from django.shortcuts import get_object_or_404, render
from django_tables2 import RequestConfig
from .models import Restaurant
from .tables import TableauRestaurant, FiltreRestaurant
from django.views.generic.detail import DetailView
import csv
from django.http import HttpResponse
def tableau_donnees(request):
    f = FiltreRestaurant(request.GET, queryset=Restaurant.objects.order_by('nom').all())
    tabrestaurants = TableauRestaurant(f)
    RequestConfig(request, paginate={"per_page":200}).configure(tabrestaurants)
    return render(request, 'restaurant/tableau_donnees.html', {"restaurants": tabrestaurants, 'filtre': f})

def cartographie_simple(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/cartographie.html', {"restaurants": restaurants})

def list_restaurant(request):
    f = FiltreRestaurant(request.GET, queryset=Restaurant.objects.all())
    return render(request, 'restaurant/tableau_donnees_trie.html', {'filtre': f})

class RestaurantDetail(DetailView):
    model = Restaurant

def full_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dump.csv"'

    writer = csv.writer(response)
    for restaurant in Restaurant.objects.all():
        writer.writerow([restaurant.num_entree, restaurant.nom, restaurant.latitude, restaurant.longitude])

    return response