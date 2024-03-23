from django.db import models
from django.utils.translation import gettext_lazy as _

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
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title


class Offering(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='offerings')
    text = models.CharField(max_length=500)
    
    def __str__(self):
        return self.text


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

class FAQ(models.Model):
    question = models.CharField(_("Question"), max_length=255)
    answer = models.TextField(_("Answer"))

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.question
    

class SiteInformation(models.Model):
    concierge_description = models.TextField(_("Concierge Company Description"), help_text=_("Description of the concierge company services."))

    def __str__(self):
        return "Site Information"
        