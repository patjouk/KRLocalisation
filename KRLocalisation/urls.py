from django.conf.urls import patterns, include, url

from django.contrib.gis import admin
from djgeojson.views import GeoJSONLayerView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KRLocalisation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('restaurant.urls')),
)
