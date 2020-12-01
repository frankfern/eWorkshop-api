from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Staff, Profile


class BaseStaffSerializer(serializers.Serializer):

    first_name = serializers.CharField(
    )
    last_name = serializers.CharField()
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Staff.objects.all())])

    ci = serializers.CharField(
        validators=[UniqueValidator(queryset=Staff.objects.all())])

    is_active = serializers.CharField(required=False)
    groups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    email = serializers.CharField(
        validators=[UniqueValidator(queryset=Staff.objects.all())])
    phone_number = serializers.CharField()
    cellphone_number = serializers.CharField()
    address = serializers.CharField()


class CreateStaffSerializaer(BaseStaffSerializer):

    password = serializers.CharField(max_length=64, min_length=8)
    password_confirmation = serializers.CharField(max_length=64, min_length=8)

    def validate(self, data):
        psswd = data['password']
        psswd_conf = data['password_confirmation']
        if psswd != psswd_conf:
            raise serializers.ValidationError("Password does not match.")
        password_validation.validate_password(psswd)

        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = Staff.objects.create(**validated_data)
        profile = Profile.objects.create(staff=user)

        return user


class ShowStaffSerializaer(BaseStaffSerializer):

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
