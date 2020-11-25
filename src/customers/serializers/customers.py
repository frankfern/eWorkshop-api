from rest_framework import serializers

from ..models import Customer


class CustomerSerializer(serializers.Serializer):

    first_name = serializers.CharField()

    last_name = serializers.CharField()

    phone_number = serializers.CharField()

    cellphone_number = serializers.CharField()
