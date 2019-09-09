from django.db import models
from django_mysql.models import JSONField

# Create your models here.
class question(models.Model):
    question = models.CharField(max_length = 4000)
    expected_answer = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'question'