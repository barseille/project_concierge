from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    """
    Modèle représentant les coordonnées des utilisateurs soumises via le formulaire de contact.
    Stocke le prénom, le nom, l'email, le téléphone et le message de l'utilisateur.
    """
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone"), max_length=15, blank=True, null=True)
    message = models.TextField(_("Message"))
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Service(models.Model):
    """
    Modèle représentant un service offert par l'entreprise.
    Contient un titre et une description du service.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class Offering(models.Model):
    """
    Modèle représentant une offre spécifique liée à un service.
    Chaque offre a un titre, une description et est liée à un service.
    """
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='offerings')
    title = models.CharField(max_length=500)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.title} - {self.service.title}'


class Testimonial(models.Model):
    """
    Modèle pour stocker les témoignages des clients.
    Inclut le nom du client, son rôle (optionnel), son message, une photo (optionnelle) et le pays.
    """
    name = models.CharField(_("Name"), max_length=100)
    role = models.CharField(_("Role"), max_length=100, blank=True, null=True)
    message = models.TextField(_("Message"))
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    country = models.CharField(_("Country"), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")

    def __str__(self):
        return self.name


class FAQ(models.Model):
    """
    Modèle pour les questions fréquentes liées à un service spécifique ou générales à tous les services.
    Comprend la question, la réponse et un indicateur pour marquer comme FAQ générale.
    """
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs', null=True, blank=True)
    question = models.CharField(_("Question"), max_length=255)
    answer = models.TextField(_("Answer"))
    is_general = models.BooleanField(default=False, help_text=_("Mark this FAQ as a general FAQ that applies to all services."))

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.question
    

class SiteInformation(models.Model):
    """
    Modèle stockant les informations générales du site, comme la description des services de conciergerie.
    """
    concierge_description = models.TextField(_("Concierge Company Description"), help_text=_("Description of the concierge company services."))

    def __str__(self):
        return "Site Information"


class HomePageSection(models.Model):
    """
    Modèle pour les sections de la page d'accueil, incluant un titre, un sous-titre, une image,
    et le texte pour jusqu'à deux boutons.
    """
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



class ExampleModel(models.Model):
    """
    Un modèle d'exemple simple avec un champ de texte.
    """
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
