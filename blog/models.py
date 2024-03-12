# # blog/models.py

# from django.db import models

# class Contact(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15, blank=True, null=True)  # Optionnel
#     message = models.TextField()
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone"), max_length=15, blank=True, null=True)
    message = models.TextField(_("Message"))
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
