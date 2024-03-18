from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _
from .models import Service, Testimonial,FAQ

def home(request):
    form = ContactForm()
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    context = {
        'form': form,
        'services': service,
        'testimonials': testimonial,
        'faqs': faqs
    }
    return render(request, 'home.html', context)



from django.core.mail import send_mail
from django.conf import settings

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
    return render(request, '_contact.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')



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


# def test(request):
#     contacts = Contact.objects.all()
#     return render(request, "test.html", {"contacts": contacts})
