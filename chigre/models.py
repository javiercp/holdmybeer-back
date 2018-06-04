from django.db import models

# Create your models here.

class Brewery(models.Model)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='')
    webpage = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ('created',)
