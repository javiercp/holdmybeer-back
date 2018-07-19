"""holdmybeer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path
from django_otp.admin import OTPAdminSite
from django.conf.urls import url, include
from chigreQL.views import PrivateGraphQLView
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)

admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('trastienda/', admin.site.urls),
    url(r'^', include('chigre.urls')),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'},name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'logged_out.html'},name='logout'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/$', TokenObtainSlidingView.as_view(), name='token_obtain_pair'),
    url(r'^api-token-auth/refresh/$', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    url(r'^graphql', PrivateGraphQLView.as_view(graphiql=True)),
]

if os.environ.get('ENABLE_DDB')=='TRUE':
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

