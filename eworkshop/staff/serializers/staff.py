from django.contrib.auth import password_validation, get_user_model
from django.http import request

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .profile import ProfileSerializer
from ..models import Profile


Staff = get_user_model()


class ListStaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ('id', 'first_name', 'last_name', 'username', 'is_active')


class ShowStaffSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Staff.objects.all())])

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Staff
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'cellphone_number',
            'address',
            'ci',
            'profile',
            'groups'
        )

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password('1234')
        instance.save()
        Profile.objects.create(staff=instance)
        return instance


class StaffChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField()

    password = serializers.CharField(
        max_length=64, min_length=8, required=True)
    password_confirmation = serializers.CharField(
        max_length=64, min_length=8, required=True)

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Password does not match.")
        password_validation.validate_password(data['password'])
        return data

    def validate_old_password(self, value):
        if not self.instance.check_password(value):
            raise serializers.ValidationError("Old password is wrong")

    def update(self, instance, validated_data):
        password = validated_data['password']
        instance.set_password(password)
        instance.change_password()
        instance.save()
        return instance
