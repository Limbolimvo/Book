from django import forms

from .models import Contact
from django.forms import ModelForm, TextInput, EmailInput


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "phone", "email", "address", "company",
                  "photo"]  # список полей, которые должны присутствовать в форме
        widgets = {
            "first_name": TextInput(attrs={
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

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance']:
            self.id = kwargs['instance'].id
        else:
            self.id = None

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        phone = self.cleaned_data.get('phone')
        for i in Contact.objects.all():
            if (first_name == i.first_name and last_name == i.last_name) and self.id != i.id:
                raise forms.ValidationError(
                    {'phone': u'Error: User with this first name and last name is already exist'})
            if i.phone == phone and self.id != i.id:
                raise forms.ValidationError({'phone': u'Error: This phone is already exits'})
        return self.cleaned_data
