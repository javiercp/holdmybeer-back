from django.conf import settings
from django.db import models
from .singletonmodel import SingletonModel
from .common import get_sentinel_user

class Pub(SingletonModel):
    updated = models.DateTimeField(auto_now=True)
    updater = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        null=True, blank=True
    )
    name = models.CharField(max_length=100, blank=True, default='')
    motto = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    address = models.TextField(blank=True, default='')
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    telephone = models.CharField(max_length=50, blank=True, default='')
    logo = models.CharField(max_length=100, blank=True, default='')
    