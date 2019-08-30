from django.db import models

# Create your models here.

class complaint(models.Model):
    user_id = models.IntegerField()
    geo_tag = models.TextField()
    description= models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length = 300, null=True)

    class Meta:
        db_table = 'complaint'