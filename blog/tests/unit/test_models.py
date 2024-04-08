import pytest


@pytest.mark.django_db
def test_contact_creation(contact):
    """
    Teste la création d'un objet Contact et vérifie si les attributs sont correctement assignés.

    Ce test unitaire s'assure que l'objet Contact créé à l'aide de la fixture 'contact'
    possède bien les valeurs attendues pour chaque champ, et que la méthode `__str__`
    retourne correctement la concaténation du prénom et du nom.
    """
    assert contact.first_name == "Chan"
    assert contact.last_name == "Sotheara"
    assert contact.email == "sotheara.chan@example.com"
    assert contact.phone == "0123456789"
    assert contact.message == "Hello, I'm interested in your services."
    assert str(contact) == "Chan Sotheara"


@pytest.mark.django_db
def test_service_creation(service):
    """
    Teste la création d'un objet Service et vérifie si les attributs sont correctement assignés.

    Ce test unitaire s'assure que l'objet Service créé à l'aide de la fixture 'service'
    possède bien les valeurs attendues pour le titre et la description, et que la méthode
    `__str__` retourne correctement le titre du service.
    """
    assert service.title == "High-End Concierge"
    assert service.description == "Providing exceptional concierge services for our discerning clients."
    assert str(service) == "High-End Concierge"


@pytest.mark.django_db
def test_offering_creation(offering):
    """
    Teste la création d'un objet Offering et vérifie si les attributs sont correctement assignés,
    ainsi que le bon retour de la méthode __str__.
    """
    assert offering.title == "Exclusive Villa Booking"
    assert offering.description == "Book an exclusive villa."
    assert offering.service.title == "High-End Concierge"  # En supposant que le titre du service soit "High-End Concierge"
    assert str(offering) == "Exclusive Villa Booking - High-End Concierge"


@pytest.mark.django_db
def test_testimonial_creation(testimonial):
    """
    Teste la création d'un objet Testimonial et vérifie si les attributs sont correctement assignés.

    Ce test unitaire s'assure que l'objet Testimonial créé à l'aide de la fixture 'testimonial'
    possède bien les valeurs attendues. Cela inclut le nom du client, ainsi que le pays d'origine.
    """
    assert str(testimonial) == "Sophorn"
    assert testimonial.country == "France"
    
@pytest.mark.django_db
def test_faq_creation(faq):
    """
    Teste la création d'un objet FAQ et vérifie si les attributs sont correctement assignés,
    ainsi que le bon retour de la méthode __str__.
    """
    assert faq.question == "What is included in the concierge service?"
    assert faq.answer == "The service includes travel planning, event booking, and exclusive access to local attractions."
    assert faq.is_general is True
    assert faq.service.title == "High-End Concierge"
    assert str(faq) == "What is included in the concierge service?"
