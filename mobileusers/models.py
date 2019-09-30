from django.db import models
from django_forcedfields import TimestampField

# Create your models here.

class mobileuser(models.Model):
    google_id = models.CharField(max_length= 30, primary_key= True)
    email = models.CharField(max_length=250, unique=True)
    nickname = models.CharField(max_length=300)
    phoneNo = models.CharField(max_length=100, null = True)
    image = models.CharField(max_length = 300, null=True)
    nic = models.CharField(max_length=12, null = True, unique= True)
    created_at = TimestampField(auto_now_add=True)
    updated_at = TimestampField(auto_now=True)
    

    class Meta:
        db_table = 'user'