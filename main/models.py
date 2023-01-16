from django.db import models


class Person(models.Model):
    name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    phone = models.PositiveIntegerField('Phone')
    email = models.CharField('Email', max_length=30)
    address = models.CharField('Address', max_length=80)
    company = models.CharField('Company', max_length=30)

    def __str__(self):
        return self.name

    class Meta:  # изменение название таблички
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
