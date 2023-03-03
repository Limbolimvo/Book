from rest_framework import serializers
from .models import Contact


class ContactViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ['id', ]


