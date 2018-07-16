from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from .common import get_sentinel_user

# Create your models here.
class PubGallery(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='')
    image = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ('created',)
