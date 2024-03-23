from modeltranslation.translator import register, TranslationOptions
from .models import Service, Testimonial, FAQ, SiteInformation, Offering

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
    
@register(Offering)
class OfferingTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('role', 'message',)

 
@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)
    
@register(SiteInformation)
class SiteInformationTranslationOptions(TranslationOptions):
    fields = ('concierge_description',)