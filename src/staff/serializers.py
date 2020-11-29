from rest_framework import serializers
from settings.settings import AUTH_USER_MODEL


class BaseStaffSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    ci = serializers.CharField()
    is_active = serializers.CharField()
    groups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class CreateStaffSerializaer(BaseStaffSerializer):

    def create(self, validated_data):

        return AUTH_USER_MODEL.objects.create(**validated_data)


class ShowStaffSerializaer(BaseStaffSerializer):

    email = serializers.CharField()
    phone_number = serializers.CharField()
    cellphone_number = serializers.CharField()
    address = serializers.CharField()

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.cellphone_number = validated_data.get(
            'cellphone_number', instance.cellphone_number),

        instance.username = validated_data.get(
            'username', instance.username)
        instance.ci = validated_data.get(
            'ci', instance.ci)
        instance.email = validated_data.get(
            'email', instance.email)
        instance.address = validated_data.get(
            'address', instance.address)
        instance.save()
        return instance
