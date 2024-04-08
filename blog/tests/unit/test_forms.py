import pytest
from blog.forms import ContactForm

@pytest.mark.django_db
def test_contact_form_valid_data():
    """
    Teste que le formulaire de contact est valide lorsque toutes les données requises sont fournies
    et conformes aux attentes de validation.
    """
    form_data = {
        'first_name': 'Jean',
        'last_name': 'Dupont',
        'email': 'jean.dupont@example.com',
        'phone': '0123456789',
        'message': 'Ceci est un message test.',
    }
    form = ContactForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_contact_form_missing_required_fields():
    """
    Teste que le formulaire de contact est invalide si des champs requis sont manquants,
    et vérifie que les messages d'erreur appropriés sont retournés.
    """
    form_data = {
        'first_name': 'Jean',
        # 'last_name' est manquant
        'email': 'jean.dupont@example.com',
        # 'message' est manquant
    }
    form = ContactForm(data=form_data)
    assert not form.is_valid()
    assert 'last_name' in form.errors
    assert 'message' in form.errors
    assert form.errors['last_name'] == ['This field is required.']
    assert form.errors['message'] == ['This field is required.']

@pytest.mark.django_db
def test_contact_form_invalid_email():
    """
    Teste la validation de l'adresse email dans le formulaire de contact.
    Vérifie que le formulaire est invalide avec une adresse email incorrecte
    et retourne le message d'erreur attendu.
    """
    form_data = {
        'first_name': 'Jean',
        'last_name': 'Dupont',
        'email': 'ceci_n_est_pas_un_email',
        'message': 'Ceci est un message test.',
    }
    form = ContactForm(data=form_data)
    assert not form.is_valid()
    assert 'email' in form.errors
    assert form.errors['email'] == ['Please enter a valid email address.']
