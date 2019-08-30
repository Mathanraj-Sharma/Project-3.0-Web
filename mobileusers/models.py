from django.db import models

# Create your models here.

class mobileusers(models.Model):
    nic = models.CharField(max_length=12, null = True)
    nickname = models.CharField(max_length=300)
    email = models.CharField(max_length=150, primary_key=True)
    phoneNo = models.CharField(max_length=100, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length = 300, null=True)

    class Meta:
        db_table = 'user'