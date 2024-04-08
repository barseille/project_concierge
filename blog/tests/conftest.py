import pytest
from blog.models import Contact, Service, Testimonial, Offering, FAQ


@pytest.fixture
def contact():
    """
    Crée et retourne une instance du modèle Contact pour les tests.

    Cet objet Contact représente les coordonnées d'un utilisateur fictif soumettant un formulaire.
    """
    return Contact.objects.create(
        first_name="Chan",
        last_name="Sotheara",
        email="sotheara.chan@example.com",
        phone="0123456789",
        message="Hello, I'm interested in your services."
    )
    
@pytest.fixture
def service():
    """
    Crée et retourne une instance du modèle Service pour les tests.

    Cet objet Service représente un service fictif offert par l'entreprise.
    """
    return Service.objects.create(
        title="High-End Concierge",
        description="Providing exceptional concierge services for our discerning clients."
    )

@pytest.fixture
def offering(service):
    """
    Crée et retourne une instance du modèle Offering pour les tests.
    
    Cet objet Offering représente une offre spécifique liée à un service.
    """
    return Offering.objects.create(
        service=service,
        title="Exclusive Villa Booking",
        description="Book an exclusive villa."
    )


@pytest.fixture
def testimonial():
    """
    Crée et retourne une instance du modèle Testimonial pour les tests.

    Cet objet Testimonial représente un témoignage de client fictif,
    utilisé pour tester la création et l'intégrité des données dans la base de données de test.
    """
    return Testimonial.objects.create(
        name="Sophorn",
        role="Client",
        message="Excellent service!",
        country="France"
    )

@pytest.fixture
def faq(service):
    """
    Crée et retourne une instance du modèle FAQ pour les tests.
    
    Cet objet FAQ représente une question fréquemment posée liée à un service.
    """
    return FAQ.objects.create(
        service=service,
        question="What is included in the concierge service?",
        answer="The service includes travel planning, event booking, and exclusive access to local attractions.",
        is_general=True
    )