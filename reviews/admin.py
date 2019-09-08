from django.contrib import admin
<<<<<<< HEAD
from django.utils import timezone
from .models import review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','queAndAnsr','geo_tag','device_signature','created_at','modified_at','days_since_creation')
    date_hierarchy = 'created_at'
    list_filter = ('created_at','modified_at')

    def days_since_creation(self,review):
        diff = timezone.now() - review.created_at
        return diff.days
    days_since_creation.short_description = 'Days Active'

admin.site.register(review,ReviewAdmin)
=======
from .models import review

# Register your models here.
admin.site.register(review)
>>>>>>> b40df385bd293c28113b6dd85ff82901664d2f40
