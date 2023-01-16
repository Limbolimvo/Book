from .models import Person
from django.forms import ModelForm, TextInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["name", "last_name", "phone", "email", "address", "company"]    #список полей, которые должны присутствовать в форме
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+380'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            "company": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Компания'
            }),
        }