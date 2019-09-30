from django.db import models
from django_forcedfields import TimestampField
from mobileusers.models import mobileuser

# Create your models here.

class complaint(models.Model):
    user = models.ForeignKey(mobileuser, on_delete = models.DO_NOTHING)
    geo_tag = models.TextField()
    description= models.CharField(max_length = 300)
    created_at = TimestampField(auto_now_add=True)
    updated_at = TimestampField(auto_now=True)
    image = models.CharField(max_length = 300, null=True)

    class Meta:
        db_table = 'complaint'