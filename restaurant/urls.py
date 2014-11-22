from django.conf.urls import patterns, include, url
from . import views
from restaurant.views import RestaurantDetail

from djgeojson.views import GeoJSONLayerView

from restaurant.models import Restaurant

urlpatterns = patterns('',
    url(r'^$', 'restaurant.views.tableau_donnees'),
    url(r'^cartographie_simple/', 'restaurant.views.cartographie_simple'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Restaurant, geometry_field='geom', properties=['nom', 'num_entree']), name='data'),
    url(r'^list$', views.list_restaurant),
    url(r'^(?P<pk>\d+)/', RestaurantDetail.as_view(template_name='restaurant/detail.html'), name='detail'),
    url(r'^dump.csv$', views.full_csv),
)