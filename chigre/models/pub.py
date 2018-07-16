from django.conf import settings
from django.db import models
from .singletonmodel import SingletonModel
from .common import get_sentinel_user

class Pub(SingletonModel):
    name = models.CharField(max_length=100, blank=True, default='')
    motto = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    address = models.TextField(blank=True, default='')
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    telephone = models.CharField(max_length=50, blank=True, default='')
    logo = models.CharField(max_length=100, blank=True, default='')
    