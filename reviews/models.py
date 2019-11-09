from django.db import models
from hotel.models import hotel
from mobileusers.models import mobileuser
from django_forcedfields import TimestampField


# Create your models here.
class review(models.Model):
    user = models.ForeignKey(mobileuser, on_delete = models.DO_NOTHING)
    # queAndAnsr = JSONField()
    qa = models.TextField()
    hotel = models.ForeignKey(hotel, on_delete = models.DO_NOTHING)
    geo_tag = models.TextField()
    device_signature= models.TextField()
    created_at = TimestampField(auto_now_add=True)
    updated_at = TimestampField(auto_now=True)

    class Meta:
        db_table = 'reviews'
