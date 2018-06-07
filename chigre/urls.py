from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from chigre import views

urlpatterns = [
    url(r'^breweries/$', views.BreweryList.as_view(), name='brewery-list'),
    url(r'^breweries/(?P<pk>[0-9]+)/$', views.BreweryDetail.as_view(), name='brewery-detail'),
    url(r'^kegtypes/$', views.KegTypeList.as_view(), name='kegtype-list'),
    url(r'^kegtypes/(?P<pk>[0-9]+)/$', views.KegTypeDetail.as_view(), name='kegtype-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
