from django.contrib import admin
from .models import question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question','expected_answer','created_at','modified_at')
    date_hierarchy = ('created_at')
    list_filter = ('id', )
    ordering = ('id',)

#QuestionAdmin.objects.order_by('id')
admin.site.register(question,QuestionAdmin)