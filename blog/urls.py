from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil
    path("", views.home, name="home"),
    
    # Page de contact
    path('contact/', views.contact_view, name='contact'),
    
    # Page de remerciement après soumission du formulaire de contact
    path('thanks/', views.thanks, name='thanks'),
    
    # Page des valeurs de l'entreprise
    path('values/', views.values, name='values'),
    
    # Page des services offerts
    path('services/', views.services, name='services'),
    
    # Page de politique de confidentialité
    path('privacy_policy/', views.get_privacy_policy, name='privacy_policy'),
    
    # Page des conditions d'utilisation
    path('terms_of_use/', views.get_terms_of_use, name='terms_of_use'),

    # URL commentée pour un détail de service et l'envoi d'email de test, pouvant être activées si nécessaire
    # path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    # path('send-test-email/', send_test_email, name='send_test_email'),
]

