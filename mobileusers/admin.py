from django.contrib import admin
from .models import mobileuser


class MobileUserAdmin(admin.ModelAdmin):
    list_display = ('google_id','nic','email','nickname','phoneNo','image','created_at','updated_at')
    search_fields = ['nickname','email']
    #list_per_page
    actions = ('change_email',)
    #list_filter // used to filter the data and it appears in side_panel

    def change_email(self,request,queryset):
        count = queryset.update(email = 'qwerty@gmail.com')
        self.message_user(request,'{} emails has updated.'.format(count))
    change_email.short_description = 'Change the email'

   

admin.site.register(mobileuser,MobileUserAdmin)