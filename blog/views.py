from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Testimonial,FAQ, SiteInformation,HomePageSection
from django.views.generic import DetailView

# Page d'accueil
def home(request):
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
    
    # Récupération du texte <p> du footer   
    site_info = SiteInformation.objects.first()  
    context = {
        'form': form,
        'site_info': site_info,
    }
    return render(request, 'contact.html', context)


def thanks(request):
    return render(request, 'thanks.html')

# Section Nos valeurs
def values(request):
    form = ContactForm()
    testimonial = Testimonial.objects.all()
    site_info = SiteInformation.objects.first()
    
    context = {
        'form': form,
        'testimonials': testimonial,
        'site_info': site_info,
    }
    return render(request, 'values.html', context)


# Vues pour les services
def services(request):
    try:
        # Récupère la première instance de Service
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
    site_info = SiteInformation.objects.first()
    context = {
        'site_info': site_info,
        }
    return render(request, 'privacy_policy.html', context)

def get_terms_of_use(request):
    site_info = SiteInformation.objects.first()
    context = {
        'site_info': site_info,
        }
    return render(request, 'terms_of_use.html', context)

# Détails de chaque service
# class ServiceDetailView(DetailView):
#     model = Service
#     template_name = 'service_detail.html'
#     context_object_name = 'service'
    
    
#     def get_context_data(self, **kwargs):
#         # Appel de la méthode de base pour obtenir le contexte
#         context = super().get_context_data(**kwargs)
        
#         # Ajout de données supplémentaires au contexte
#         context['service_faqs'] = self.object.faqs.all()
#         context['general_faqs'] = FAQ.objects.filter(is_general=True)
#         context['form'] = ContactForm()
#         context['testimonials'] = Testimonial.objects.all()
#         context['site_info'] = SiteInformation.objects.first()
#         return context


# from django.core.mail import send_mail
# from django.http import HttpResponse

# def send_test_email(request):
#     send_mail(
#         'Sujet de test',
#         'Voici le message.',
#         'from@example.com',
#         ['to@example.com'],
#         fail_silently=False,
#     )
#     return HttpResponse("Email envoyé avec succès !")

