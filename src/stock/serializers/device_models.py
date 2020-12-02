from rest_framework import serializers


from ..models import DeviceModel


class DeviceModelSerializer(serializers.ModelSerializer):
    model = DeviceModel
    fields = '__all__'
