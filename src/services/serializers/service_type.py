from rest_framework import serializers


from ..models import ServiceType


class ServiceTypeSerializer(serializers.ModelSerializer):
    model = ServiceType
    fields = '__all__'
