from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from chigre import views

urlpatterns = [
    url(r'^breweries/$', views.BreweryList.as_view(), name='brewery-list'),
    url(r'^breweries/(?P<pk>[0-9]+)/$', views.BreweryDetail.as_view(), name='brewery-detail'),
    url(r'^kegtypes/$', views.KegTypeList.as_view(), name='kegtype-list'),
    url(r'^kegtypes/(?P<pk>[0-9]+)/$', views.KegTypeDetail.as_view(), name='kegtype-detail'),
    url(r'^beertypes/$', views.BeerTypeList.as_view(), name='beertype-list'),
    url(r'^beertypes/(?P<pk>[0-9]+)/$', views.BeerTypeDetail.as_view(), name='beertype-detail'),
    url(r'^beers/$', views.BeerList.as_view(), name='beer-list'),
    url(r'^beers/(?P<pk>[0-9]+)/$', views.BeerDetail.as_view(), name='beer-detail'),
    url(r'^beers/extended$', views.BeerList.as_view(), name='beer-list-ex'),
    url(r'^beers/(?P<pk>[0-9]+)/extended$', views.BeerDetail.as_view(), name='beer-detail-ex'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
