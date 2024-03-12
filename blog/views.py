from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _
from .models import Contact

def home(request):
    form = ContactForm()  # Initialise your form here to display it on the homepage
    return render(request, 'home.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
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

def test(request):
    contacts = Contact.objects.all()
    return render(request, "test.html", {"contacts": contacts})
