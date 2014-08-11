from django.shortcuts import render
from .models import Restaurant

def tableau_donnees(request):
    restaurants = Restaurant.objects.order_by('num_entree')
    return render(request, 'restaurant/tableau_donnees.html', {"restaurants": Restaurant.objects.all()})
