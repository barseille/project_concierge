
from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .models import Contact

# Définir un validateur pour les noms
name_validator = RegexValidator(
    regex=r'^[a-zA-ZÀ-ÿ\s-]+$',
    message=_("Please enter a valid name with letters only."),
)

# Validator for phone numbers
phone_validator = RegexValidator(
    regex=r'^[\+]?[0-9\s]+$',
    message=_("Please enter a valid phone number with digits only."),
)

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        validators=[name_validator],
        # widget=forms.TextInput(attrs={'class': 'rounded-md border-gray-300 focus:border-yellow-500 focus:ring focus:ring-yellow-500 focus:ring-opacity-50'}),
        widget=forms.TextInput(attrs={'class': 'input-style', 'placeholder': _('First Name*')}),
        label='',
    )
    last_name = forms.CharField(
        validators=[name_validator],
        widget=forms.TextInput(attrs={'class': 'input-style', 'placeholder': _('Last Name*')}),
        label='',
    )
    email = forms.EmailField(
        label='', 
        error_messages={
            'invalid': _("Please enter a valid email address."),
            'required': _("This field is required."),
        },
        widget=forms.EmailInput(attrs={'class': 'input-style', 'placeholder': _('Email*')}),
    )
    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(attrs={'class': 'input-style', 'placeholder': _('Phone')}),
        label='',
        required=False,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'input-style-message rounded-md',
            'rows': 10, 
            'maxlength': '1000'}),
       
        # widget=forms.Textarea(attrs={'class': 'rounded-md border-gray-300 focus:border-yellow-500 focus:ring focus:ring-yellow-500 focus:ring-opacity-50 text-red', 'maxlength': '1000'}),
        label=_("Message*"),
    )
    
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
