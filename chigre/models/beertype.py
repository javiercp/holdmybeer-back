from django.conf import settings
from django.db import models

# Create your models here.
class BeerType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ('name',)
