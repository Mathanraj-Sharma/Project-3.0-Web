from django.contrib import admin
from django.utils import timezone
from .models import review
from .models import hotel

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','qa','geo_tag','hotel_id','device_signature','created_at','updated_at')
    date_hierarchy = 'created_at'
    list_filter = ('created_at','updated_at')

    """"def days_since_creation(self,review):
        diff = timezone.now() - review.created_at
        return diff.days
    days_since_creation.short_description = 'Days Active'"""
    def hotel_id(self, obj):
        return obj.hotel.id

admin.site.register(review,ReviewAdmin)