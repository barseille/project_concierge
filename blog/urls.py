from django.urls import path
from . import views
# from .views import send_test_email

urlpatterns = [
    path("", views.home, name="home"),
    path('contact/', views.contact_view, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    path('our_values/', views.our_values, name='our_values'),
    path('services/', views.services, name='services'),

    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    
    
    
    # path('send-test-email/', send_test_email, name='send_test_email'),
    # path('test/', views.test, name="test")
]
