from rest_framework import serializers


from ..models import DeviceType


class DeviceTypeSerializer(serializers.ModelSerializer):
    model = DeviceType
    fields = '__all__'
