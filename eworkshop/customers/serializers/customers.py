from rest_framework import serializers

from ..models import Customer


class CustomerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        """
        docstring
        """
        model = Customer
        fields = "__all__"
