from rest_framework import serializers

from ..models import Customer


class CustomerCreateSerializer(serializers.Serializer):

    first_name = serializers.CharField()

    last_name = serializers.CharField()

    phone_number = serializers.CharField()

    cellphone_number = serializers.CharField()

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.cellphone_number = validated_data.get(
            'cellphone_number', instance.cellphone_number)
        instance.save()
        return instance
