from django.db import models
from django_forcedfields import TimestampField

# Create your models here.
class hotel(models.Model):
    hotel_name = models.CharField(max_length=1000)
    # longtitude = models.DecimalField(max_digits=10, decimal_places=7)
    # latitude = models.DecimalField(max_digits=10, decimal_places=7)
    geo_tag = models.TextField()
    address = models.CharField(max_length=3000)
    created_at = TimestampField(auto_now_add=True)
    updated_at = TimestampField(auto_now=True)

    class Meta:
        db_table = 'hotel'