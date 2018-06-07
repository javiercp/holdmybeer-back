from django.conf import settings
from django.db import models
from .common import get_sentinel_user

# Create your models here.
class KegType(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    name = models.CharField(max_length=100, unique=True)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    pints = models.IntegerField()
    canyas = models.IntegerField()
    
    class Meta:
        ordering = ('created',)
