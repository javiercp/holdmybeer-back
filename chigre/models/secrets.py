from django.db import models
from .singletonmodel import SingletonModel

class Secrets(SingletonModel):
    maps_key = models.CharField(max_length=100, blank=True, default='')

    