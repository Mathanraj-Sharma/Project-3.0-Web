from django.contrib import admin
from .models import complaint
from django.utils import timezone


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','geo_tag','description','created_at','modified_at','image','days_since_creation')
    date_hierarchy = 'created_at'
    list_filter = ('user_id','geo_tag')
    ordering = ('id',)

    def days_since_creation(self,complaint):
        diff = timezone.now() - complaint.created_at
        return diff.days
        
# Register your models here.
admin.site.register(complaint, ComplaintAdmin)