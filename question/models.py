from django.db import models

# Create your models here.
class question(models.Model):
    question = models.CharField(max_length = 4000)
    expected_answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'question'