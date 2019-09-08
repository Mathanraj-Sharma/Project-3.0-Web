from django.contrib import admin
from .models import mobileuser

<<<<<<< HEAD

class MobileUserAdmin(admin.ModelAdmin):
    list_display = ('nic','email','nickname','phoneNo','image','created_at','modified_at')
    search_fields = ['nickname','email']
    #list_per_page
    actions = ('change_email',)
    #list_filter // used to filter the data and it appears in side_panel

    def change_email(self,request,queryset):
        count = queryset.update(email = 'qwerty@gmail.com')
        self.message_user(request,'{} emails has updated.'.format(count))
    change_email.short_description = 'Change the email'

   

admin.site.register(mobileuser,MobileUserAdmin)
=======
# Register your models here.
admin.site.register(mobileuser)
>>>>>>> b40df385bd293c28113b6dd85ff82901664d2f40
