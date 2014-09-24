from django.conf.urls import patterns, include, url
from . import views

from djgeojson.views import GeoJSONLayerView

from restaurant.models import Restaurant

urlpatterns = patterns('',
    url(r'^$', 'restaurant.views.tableau_donnees'),
    url(r'^cartographie_simple/', 'restaurant.views.cartographie_simple'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Restaurant, geometry_field='geom'), name='data'),
)