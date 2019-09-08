from django.contrib import admin
from .models import complaint
<<<<<<< HEAD
from django.utils import timezone
=======
>>>>>>> b40df385bd293c28113b6dd85ff82901664d2f40


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','geo_tag','description','created_at','modified_at','image','days_since_creation')
    date_hierarchy = 'created_at'
    list_filter = ('user_id','geo_tag')
    ordering = ('id',)

    def days_since_creation(self,complaint):
        diff = timezone.now() - complaint.created_at
        return diff.days
        
# Register your models here.
<<<<<<< HEAD
admin.site.register(complaint, ComplaintAdmin)
=======
admin.site.register(complaint)
>>>>>>> b40df385bd293c28113b6dd85ff82901664d2f40
