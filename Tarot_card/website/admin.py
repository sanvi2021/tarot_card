from django.contrib import admin
from . models import *
# Register your models here.

# admin.site.register(contact_lead)
@admin.register(contact_lead)
class Contact_list(admin.ModelAdmin):
    list_display= ('id','name','email_id','phone_number')

