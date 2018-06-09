from django.conf import settings
from django.db import models
from .common import get_sentinel_user

# Create your models here.
class Beer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='')
    abv = models.DecimalField(max_digits=5, decimal_places=2)
    webpage = models.CharField(max_length=100, blank=True, default='')
    logo = models.CharField(max_length=100, blank=True, default='')
    brewery = models.ForeignKey(
        'Brewery',
        on_delete=models.CASCADE,
    )
    beertype = models.ForeignKey(
        'BeerType',
        on_delete=models.CASCADE,
    )
    
    class Meta:
        ordering = ('created',)
