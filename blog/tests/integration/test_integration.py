import pytest
from django.urls import reverse
from blog.models import Contact

@pytest.mark.django_db
def test_contact_form_submission(client):
    """
    Test d'intégration pour le formulaire de contact.
    Vérifie que le formulaire soumis crée un nouvel enregistrement dans la base de données.
    """
    url = reverse('contact')
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'message': 'This is a test message.',
    }
    
    response = client.post(url, data)
    
    # Vérifiez la redirection après la soumission du formulaire
    assert response.status_code == 302
    
    # Vérifiez que les données sont correctement enregistrées dans la base de données
    contact = Contact.objects.last()
    assert contact.first_name == 'John'
    assert contact.email == 'john.doe@example.com'
    assert contact.message == 'This is a test message.'
