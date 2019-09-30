from django.db import models
from django_mysql.models import JSONField
from django_forcedfields import TimestampField

# Create your models here.
class question(models.Model):
    question = models.CharField(max_length = 4000)
    expected_answer = JSONField()
    created_at = TimestampField(auto_now_add=True)
    updated_at = TimestampField(auto_now=True)

    
    class Meta:
        db_table = 'question'