import pytest
from django.urls import reverse
from blog.models import Service, SiteInformation


@pytest.mark.django_db
def test_home_view(client):
    """
    Teste si la vue home renvoie un code de statut HTTP 200 (succès),
    et vérifie que le contexte de la réponse contient les objets 'form' et 'services'.
    """
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context
    assert 'services' in response.context


@pytest.mark.django_db
def test_contact_view_get(client):
    """
    Teste la vue contact pour une requête GET.

    Ce test vérifie que la vue de contact répond correctement à une requête GET
    en retournant un code de statut 200. Il s'assure également que le contexte de
    réponse contient bien un objet 'form', ce qui indique que le formulaire de contact
    est correctement transmis au template pour être affiché à l'utilisateur.
    """
    url = reverse('contact')
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context


@pytest.mark.django_db
def test_contact_view_post_valid(client):
    """
    Teste la vue contact pour une requête POST avec des données valides.

    Ce test soumet un formulaire de contact valide via une requête POST à la vue de contact.
    Il vérifie que la vue traite correctement les données valides en redirigeant l'utilisateur
    vers une nouvelle URL, typiquement une page de remerciement. Le code de statut 302 indique
    cette redirection. De plus, le test s'assure que l'URL de redirection est bien celle de la
    page de remerciements, ce qui confirme le traitement réussi du formulaire de contact.
    """
    url = reverse('contact')
    response = client.post(url, {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'message': 'Hello, this is a test message.',
    })
    
    # Redirection attendue si le formulaire est valide
    assert response.status_code == 302  
    assert response.url == reverse('thanks')


@pytest.mark.django_db
def test_contact_view_post_invalid(client):
    """
    Teste la vue de contact pour une soumission POST invalide.

    Ce test simule l'envoi d'un formulaire de contact vide à la vue de contact
    et vérifie plusieurs comportements attendus :
    - Le code de statut HTTP 200 est renvoyé, car la page doit se recharger avec des erreurs de formulaire.
    - Le contexte de la réponse doit contenir un objet 'form'.
    - Le formulaire récupéré du contexte ne doit pas être valide ('is_valid' doit retourner False).
    - Les champs 'first_name', 'email', et 'message' doivent contenir des erreurs, car ils sont requis mais n'ont pas été remplis.
    - Un message d'erreur spécifique ("This field is required.") doit être présent dans les erreurs de ces champs requis.

    Ce test assure que les validations côté serveur fonctionnent comme prévu pour le formulaire de contact,
    et que les utilisateurs reçoivent des feedbacks appropriés lorsqu'ils soumettent des formulaires incomplets.
    """
    url = reverse('contact')
    
    # Soumission d'un formulaire vide
    response = client.post(url, {})
    
    # Doit revenir à la page de contact avec des erreurs de formulaire
    assert response.status_code == 200  
    assert 'form' in response.context
    form = response.context['form']
    assert form.is_valid() is False
   
    assert 'first_name' in form.errors
    assert 'email' in form.errors
    assert 'message' in form.errors
    
    expected_error_message = "This field is required."
    assert any(expected_error_message in error for error in form.errors.values())

    

@pytest.mark.django_db
def test_thanks_view(client):
    """
    Teste si la vue thanks renvoie un code de statut HTTP 200 (succès),
    et vérifie que le contenu de la réponse contient un message de remerciement spécifique.
    """
    url = reverse('thanks')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Your message has been successfully sent. We will contact you soon.' in response.content.decode()
    

@pytest.mark.django_db
def test_services_view_success(client):
    """
    Teste si la vue services renvoie un code de statut HTTP 200
    et vérifie que le contexte de la réponse contient les objets 'service' et 'site_info'.
    """
    # Créer un objet SiteInformation pour le test
    SiteInformation.objects.create(concierge_description="Description de test")
    
    # Créer un objet Service pour le test
    Service.objects.create(title="Service Test", description="Description de service test")

    url = reverse('services')
    response = client.get(url)
    assert response.status_code == 200
    assert 'service' in response.context
    assert 'site_info' in response.context


@pytest.mark.django_db
def test_services_view_no_service(client):
    """
    Teste le comportement de la vue services en l'absence de services.
    """
    # Assurez-vous qu'aucun objet Service n'existe
    Service.objects.all().delete()
    
    # Créer un objet SiteInformation pour le test
    SiteInformation.objects.create(concierge_description="Description de test")

    url = reverse('services')
    response = client.get(url)
    assert response.status_code == 200
    assert 'service' not in response.context or response.context['service'] is None

 
@pytest.mark.django_db
def test_get_privacy_policy_view(client):
    """
    Teste si la vue get_privacy_policy renvoie un code de statut HTTP 200
    et vérifie que le contexte de la réponse contient l'objet 'site_info'.
    """
    # Créer un objet SiteInformation pour le test
    SiteInformation.objects.create(concierge_description="Description de test pour politique de confidentialité")

    url = reverse('privacy_policy')  
    response = client.get(url)
    assert response.status_code == 200
    assert 'site_info' in response.context


@pytest.mark.django_db
def test_get_terms_of_use_view(client):
    """
    Teste si la vue get_terms_of_use renvoie un code de statut HTTP 200
    et vérifie que le contexte de la réponse contient l'objet 'site_info'.
    """
    # Créer un objet SiteInformation pour le test
    SiteInformation.objects.create(concierge_description="Description de test pour conditions d'utilisation")

    url = reverse('terms_of_use')  
    response = client.get(url)
    assert response.status_code == 200
    assert 'site_info' in response.context


    
    


