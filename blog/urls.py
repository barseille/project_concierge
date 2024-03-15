from django.urls import path
from . import views
# from .views import send_test_email

urlpatterns = [
    path("", views.home, name="home"),
    path('contact/', views.contact_view, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    
    
    # path('send-test-email/', send_test_email, name='send_test_email'),
    # path('test/', views.test, name="test")
]
