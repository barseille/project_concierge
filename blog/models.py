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


class Service(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
