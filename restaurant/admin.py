from django.contrib.gis import admin
from .models import Restaurant

admin.site.register(Restaurant, admin.OSMGeoAdmin)