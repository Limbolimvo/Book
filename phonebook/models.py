from django.contrib.auth.models import User
from django.db import models


class MyUser(User):
    # username = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    # my_name = models.CharField('Name', max_length=30)
    # last_name = models.CharField('Last name', max_length=30)
    phone = models.CharField('Phone', max_length=30, null=False, blank=False, unique=True)
    #email = models.EmailField('Email', max_length=50)
    address = models.CharField('Address', max_length=80)
    photo = models.ImageField('Photo', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Contact(models.Model):
    name = models.CharField('Name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    phone = models.CharField('Phone', max_length=30, null=False, blank=False)
    email = models.EmailField('Email', max_length=50)
    address = models.CharField('Address', max_length=80)
    company = models.CharField('Company', max_length=30)
    photo = models.ImageField('Photo', upload_to='images/', null=True, blank=True)
    owner = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:  # изменение название таблички
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
