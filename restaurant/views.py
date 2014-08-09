from django.shortcuts import render

def tableau_donnees(request):

    return render(request, 'restaurant/tableau_donnees.html', {})
