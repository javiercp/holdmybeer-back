from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Brewery(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='')
    webpage = models.CharField(max_length=100, blank=True, default='')
    logo = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ('created',)
