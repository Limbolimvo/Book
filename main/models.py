from django.db import models


class Person(models.Model):
    name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    phone = models.CharField('Номер телефона', max_length=30, null=False, blank=False, unique=True)
    email = models.EmailField('Электронная почта', max_length=50)
    address = models.CharField('Адрес', max_length=80)
    company = models.CharField('Компания', max_length=30)
    photo = models.ImageField('Фото', upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:  # изменение название таблички
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class MyUser(models.Model):
    name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    phone = models.CharField('Номер телефона', max_length=30, null=False, blank=False, unique=True)
    email = models.EmailField('Электронная почта', max_length=50)
    address = models.CharField('Адрес', max_length=80)
    company = models.CharField('Компания', max_length=30)
    photo = models.ImageField('Фото', upload_to='images/', null=True, blank=True)
