from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from chigre import views

urlpatterns = [
    url(r'^breweries/$', views.brewery_list),
    url(r'^breweries/(?P<pk>[0-9]+)/$', views.brewery_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
