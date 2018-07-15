from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from chigre import views

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='HoldMyBeer API')

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^schema/$', schema_view),
    url(r'^breweries/$', views.BreweryList.as_view(), name='brewery-list'),
    url(r'^breweries/(?P<pk>[0-9]+)/$', views.BreweryDetail.as_view(), name='brewery-detail'),
    url(r'^kegtypes/$', views.KegTypeList.as_view(), name='kegtype-list'),
    url(r'^kegtypes/(?P<pk>[0-9]+)/$', views.KegTypeDetail.as_view(), name='kegtype-detail'),
    url(r'^beertypes/$', views.BeerTypeList.as_view(), name='beertype-list'),
    url(r'^beertypes/(?P<pk>[0-9]+)/$', views.BeerTypeDetail.as_view(), name='beertype-detail'),
    url(r'^beers/$', views.BeerList.as_view(), name='beer-list'),
    url(r'^beers/(?P<pk>[0-9]+)/$', views.BeerDetail.as_view(), name='beer-detail'),
    url(r'^kegs/$', views.KegList.as_view(), name='keg-list'),
    url(r'^kegs/(?P<pk>[0-9]+)/$', views.KegDetail.as_view(), name='keg-detail'),
    url(r'^taptypes/$', views.TapTypeList.as_view(), name='taptype-list'),
    url(r'^taptypes/(?P<pk>[0-9]+)/$', views.TapTypeDetail.as_view(), name='taptype-detail'),
    url(r'^taps/$', views.TapList.as_view(), name='tap-list'),
    url(r'^taps/(?P<pk>[0-9]+)/$', views.TapDetail.as_view(), name='tap-detail'),
    url(r'^beers/expanded/$', views.BeerListEx.as_view(), name='beer-list-ex'),
    url(r'^beers/(?P<pk>[0-9]+)/expanded/$', views.BeerDetailEx.as_view(), name='beer-detail-ex'),
    url(r'^kegs/expanded/$', views.KegListEx.as_view(), name='keg-list-ex'),
    url(r'^kegs/(?P<pk>[0-9]+)/expanded/$', views.KegDetailEx.as_view(), name='keg-detail-ex'),
    url(r'^taps/expanded/$', views.TapListEx.as_view(), name='tap-list-ex'),
    url(r'^taps/(?P<pk>[0-9]+)/expanded/$', views.TapDetailEx.as_view(), name='tap-detail-ex'),
    url(r'^pub/$', views.PubDetail.as_view(), name='pub-info'),
    url(r'^secrets/$', views.SecretsDetail.as_view(), name='secrets-info'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
