from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('last_name' , 'first_name', 'email', 'phone')

admin.site.register(Contact, ContactAdmin)
