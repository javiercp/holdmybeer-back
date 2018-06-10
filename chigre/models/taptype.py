from django.conf import settings
from django.db import models

# Create your models here.
class TapType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ('name',)
