from django.db import models
from django_mysql.models import JSONField
from hotel.models import hotel

# Create your models here.
class review(models.Model):
    user_id = models.IntegerField()
    queAndAnsr = JSONField()
    hotel = models.ForeignKey(hotel, on_delete = models.DO_NOTHING)
    geo_tag = models.TextField()
    device_signature= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'review'
