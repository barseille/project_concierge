from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('contact/', views.contact_view, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    path('values/', views.values, name='values'),
    path('services/', views.services, name='services'),
    path('privacy_policy/', views.get_privacy_policy, name='privacy_policy'),
    path('terms_of_use/', views.get_terms_of_use, name='terms_of_use'),

    # path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    # path('send-test-email/', send_test_email, name='send_test_email'),
]
