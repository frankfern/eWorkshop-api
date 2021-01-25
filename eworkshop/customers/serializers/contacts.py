from rest_framework import serializers

from ..models import Contact, Customer


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'customer', 'description', 'created']
