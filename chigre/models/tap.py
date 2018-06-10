from django.conf import settings
from django.db import models
from .common import get_sentinel_user

# Create your models here.
class Tap(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    number = models.IntegerField()
    photo = models.CharField(max_length=100, blank=True, default='')
    keg = models.ForeignKey(
        'Keg',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    taptype = models.ForeignKey(
        'TapType',
        on_delete=models.CASCADE,
    )
    
    class Meta:
        ordering = ('created',)
