from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Testimonial,FAQ, SiteInformation,HomePageSection
# from django.views.generic import DetailView


def home(request):
    """
    Vue pour la page d'accueil. Affiche un formulaire de contact, les services disponibles,
    les témoignages, les informations du site, les FAQs générales, et la section principale de la page d'accueil.
    """
    form = ContactForm()
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    site_info = SiteInformation.objects.first()
    general_faqs = FAQ.objects.filter(is_general=True)
    homepage_section = HomePageSection.objects.first()
    
    context = {
        'form': form,
        'services': service,
        'testimonials': testimonial,
        'general_faqs': general_faqs,
        'site_info': site_info,
        'homepage_section': homepage_section,
        
    }
    return render(request, 'home.html', context)


def contact_view(request):
    """
    Traite les soumissions du formulaire de contact. En cas de succès, envoie un email avec les détails
    du message et redirige vers la page de remerciement. En cas d'échec, affiche des messages d'erreur.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            # Extraction des données nettoyées
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Préparation de l'email
            subject = f'Message de {first_name}'
            message = f'Vous avez reçu un message de {email} : \n\n{message}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, email_from, recipient_list)
            
            try:
                form.save()
                messages.success(request, _('Your message has been successfully sent!'))
                return redirect('thanks')
            
            except Exception as e:
                messages.error(request, _('An error occurred while sending your message.'))
    else:
        form = ContactForm()
      
    site_info = SiteInformation.objects.first()  
    context = {
        'form': form,
        'site_info': site_info,
    }
    return render(request, 'contact.html', context)


def thanks(request):
    """
    Affiche une page de remerciement après l'envoi réussi d'un formulaire de contact.
    """
    return render(request, 'thanks.html')


def values(request):
    """
    Vue pour la page 'Nos valeurs'. Affiche des témoignages et des informations sur l'entreprise.
    """
    form = ContactForm()
    testimonial = Testimonial.objects.all()
    site_info = SiteInformation.objects.first()
    
    context = {
        'form': form,
        'testimonials': testimonial,
        'site_info': site_info,
    }
    return render(request, 'values.html', context)


def services(request):
    """
    Affiche une liste des services offerts par l'entreprise.
    """
    try:
        service = Service.objects.first()  
    except Service.DoesNotExist:
        service = None

    site_info = SiteInformation.objects.first()
    
    context = {
        'service': service,
        'site_info': site_info,
    }
    return render(request, 'services.html', context)


def get_privacy_policy(request):
    """
    Affiche la politique de confidentialité du site.
    """
    site_info = SiteInformation.objects.first()
    context = {
        'site_info': site_info,
        }
    return render(request, 'privacy_policy.html', context)


def get_terms_of_use(request):
    """
    Affiche les termes et conditions d'utilisation du site.
    """
    site_info = SiteInformation.objects.first()
    context = {
        'site_info': site_info,
        }
    return render(request, 'terms_of_use.html', context)
