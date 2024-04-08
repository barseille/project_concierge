from modeltranslation.translator import register, TranslationOptions
from .models import Service, Testimonial, FAQ, SiteInformation, Offering, HomePageSection

""" 
Options de traduction pour tous les modèles
Permet la traduction des champs pour supporter 
le multilangue dans l'application
"""

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
    
@register(Offering)
class OfferingTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('role', 'message',)
 
@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)
    
@register(SiteInformation)
class SiteInformationTranslationOptions(TranslationOptions):
    fields = ('concierge_description',)
    
@register(HomePageSection)
class HomePageSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'first_button_text', 'second_button_text',)