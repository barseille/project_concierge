from django.contrib import admin
from .models import Contact, Service, Testimonial, FAQ, SiteInformation, Offering, HomePageSection


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('last_name' , 'first_name', 'email', 'phone')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
 

@admin.register(Testimonial) 
class TestimonialAdmin(admin.ModelAdmin):
    '''
    Cette classe TestimonialAdmin ajoute une fonction message_preview qui affiche les 50 premiers caractères du message du témoignage dans la liste d'administration, utile pour avoir un aperçu rapide des témoignages sans avoir à ouvrir chaque entrée.
    '''  
    list_display = ('name', 'role', 'message_preview')
    
    def message_preview(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = "Message Preview"

 
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'is_general')
    list_filter = ('service', 'is_general')
    
@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    list_display = ('concierge_description',)
    

@admin.register(Offering)
class OfferingAdmin(admin.ModelAdmin):
    list_display = ('text', 'service')
    list_filter = ('service',)


@admin.register(HomePageSection)
class HomePageSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    

# admin.site.register(Contact, ContactAdmin)
# admin.site.register(Service)
# admin.site.register(Testimonial, TestimonialAdmin)
# admin.site.register(FAQ, FAQAdmin)
