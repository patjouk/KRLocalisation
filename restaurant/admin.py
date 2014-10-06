from django.contrib.gis import admin
from .models import Restaurant, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class RestaurantAdmin(admin.OSMGeoAdmin):
    inlines = [PhotoInline]

admin.site.register(Restaurant, RestaurantAdmin)