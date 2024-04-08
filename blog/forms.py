from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .models import Contact

class ContactForm(forms.ModelForm):
    """
    Formulaire pour la soumission de contact utilisé dans la page de contact.
    
    Utilise des validateurs personnalisés pour s'assurer que le nom ne contient que des lettres 
    et que le numéro de téléphone est valide. Le formulaire est lié au modèle Contact pour 
    enregistrer les soumissions directement dans la base de données.
    """
    
    # Définir un validateur pour les noms
    name_validator = RegexValidator(
        regex=r'^[a-zA-ZÀ-ÿ\s-]+$',
        message=_("Please enter a valid name with letters only."),
    )

    # Validateur pour les numéros de téléphone
    phone_validator = RegexValidator(
        regex=r'^[\+]?[0-9\s]+$',
        message=_("Please enter a valid phone number with digits only."),
    )

    first_name = forms.CharField(
        validators=[name_validator],
        widget=forms.TextInput(attrs={'class': 'input-style', 'placeholder': _('First Name*')}),
        label='',
        error_messages={'required': _("This field is required.")},
    )
    last_name = forms.CharField(
        validators=[name_validator],
        widget=forms.TextInput(attrs={'class': 'input-style', 'placeholder': _('Last Name*')}),
        label='',
        error_messages={'required': _("This field is required.")},
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
        label=_("Message*"),
    )
    
    class Meta:
        """
        Meta-classe pour spécifier le modèle lié et les champs à utiliser dans le formulaire.
        """
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
