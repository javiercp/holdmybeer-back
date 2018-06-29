from django.db import models
from .singletonmodel import SingletonModel

class Pub(SingletonModel):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    address = models.TextField(blank=True, default='')
    webpage = models.CharField(max_length=100, blank=True, default='')
    logo = models.CharField(max_length=100, blank=True, default='')
    