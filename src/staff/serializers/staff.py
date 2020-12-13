from django.contrib.auth import password_validation, get_user_model
from django.contrib.auth.models import Group


from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from ..models import Profile
from . import GroupSerializer


Staff = get_user_model()


class ListStaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'username', 'is_active')


class ShowStaffSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Staff.objects.all())])

    class Meta:
        model = Staff
        exclude = ('password',)


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
