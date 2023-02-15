from .models import Contact, User
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(
        read_only=True,
    )

    class Meta:
        model = Contact
        fields = ["name", "owner"]
        # exclude = ["phone",]
