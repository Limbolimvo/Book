from django.db import models
from django.conf import settings
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField('Name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    phone = models.CharField('Phone', max_length=30, null=False, blank=False)
    email = models.EmailField('Email', max_length=50)
    address = models.CharField('Address', max_length=80)
    company = models.CharField('Company', max_length=30)
    photo = models.ImageField('Photo', null=True, blank=True, upload_to='images/')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:  # изменение название таблички
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def get_absolute_url(self):
        return reverse('contact_details', args=[str(self.id)])