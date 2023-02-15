from .models import Contact, MyUser
from django.forms import ModelForm, TextInput, EmailInput


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "last_name", "phone", "email", "address", "company",
                  "photo"]  # список полей, которые должны присутствовать в форме
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            "address": TextInput(attrs={
                'class': 'form-control'
            }),
            "company": TextInput(attrs={
                'class': 'form-control'
            }),
        }
