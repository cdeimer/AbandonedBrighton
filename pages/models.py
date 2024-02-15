import datetime
from django.db import models
from django.utils import timezone
from django.utils.text import slugify 

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True) 
    last_updated = models.DateTimeField(auto_now=True)
    body = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def was_updated_recently(self):
        return self.last_updated >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name