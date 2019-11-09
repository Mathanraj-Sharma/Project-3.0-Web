from django.db import models
from django_forcedfields import TimestampField
from django.utils.text import slugify
from django.urls import reverse,URLPattern

# Create your models here.
class hotel(models.Model):
    hotel_name = models.CharField(max_length=1000)
    geo_tag = models.TextField()
    address = models.CharField(max_length=3000)
    created_at = TimestampField(auto_now_add=True)
    updated_at = TimestampField(auto_now=True)

        
    def get_absolute_url(self):
        return f"/hotel/hotel/{self.id}/"
 
    class Meta:
        db_table = 'hotels'
        