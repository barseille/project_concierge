from django.db import models
from django.utils.translation import gettext_lazy as _


# Coordonnées des utilisateurs via le formulaire
class Contact(models.Model):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone"), max_length=15, blank=True, null=True)
    message = models.TextField(_("Message"))
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title


# Section liste offres proposées par service
class Offering(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='offerings')
    title = models.CharField(max_length=500)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.title} - {self.service.title}'

# Section témoignages
class Testimonial(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    role = models.CharField(_("Role"), max_length=100, blank=True, null=True)
    message = models.TextField(_("Message"))
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")

    def __str__(self):
        return self.name


# Section questions/réponses
class FAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs', null=True, blank=True)
    question = models.CharField(_("Question"), max_length=255)
    answer = models.TextField(_("Answer"))
    is_general = models.BooleanField(default=False, help_text=_("Mark this FAQ as a general FAQ that applies to all services."))

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.question
    
# Texte du footer
class SiteInformation(models.Model):
    concierge_description = models.TextField(_("Concierge Company Description"), help_text=_("Description of the concierge company services."))

    def __str__(self):
        return "Site Information"


# Section image de présentation de la page d'accueil
class HomePageSection(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    subtitle = models.TextField(_("Subtitle"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to='images/')
    first_button_text = models.CharField(_("First Button Text"), max_length=50, blank=True, null=True)
    second_button_text = models.CharField(_("Second Button Text"), max_length=50, blank=True, null=True)
    
    
    class Meta:
        verbose_name = _("Home Page Section")
        verbose_name_plural = _("Home Page Sections")

    def __str__(self):
        return self.title

        