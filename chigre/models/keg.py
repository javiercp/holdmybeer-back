from django.conf import settings
from django.db import models
from .common import get_sentinel_user

# Create your models here.
class Keg(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    pintprice = models.DecimalField(max_digits=5, decimal_places=2)
    canyaprice = models.DecimalField(max_digits=5, decimal_places=2)
    fullweight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    emptyweight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    actualweight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    beer = models.ForeignKey(
        'Beer',
        on_delete=models.CASCADE,
    )
    kegtype = models.ForeignKey(
        'KegType',
        on_delete=models.CASCADE,
    )
    
    class Meta:
        ordering = ('created',)
