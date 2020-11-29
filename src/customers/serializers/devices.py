from django.db.models import fields
from rest_framework import serializers

from ..models import CustomerDevice


class DevicefSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerDevice
        fields = ['customer', 'device_model', 'description', 'sn']

    # customer = serializers.IntegerField()
    # device_model =  serializers.IntegerField()
    # description = serializers.CharField()
    # sn = serializers.CharField()

    # def create(self, validated_data):

    #     return CustomerDevice.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.customer = validated_data.get(
    #         'customer', instance.customer)
    #     instance.device_model = validated_data.get(
    #         'device_model', instance.device_model)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.sn = validated_data.get(
    #         'sn', instance.sn),

    #     instance.save()
    #     return instance
