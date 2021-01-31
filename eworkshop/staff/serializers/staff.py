from django.contrib.auth import password_validation, get_user_model

from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from .profile import ProfileSerializer
from eworkshop.tasks.tasks import request_reset_password_email
from ..tokens import EmailToken
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


class PasswordSerializer(serializers.Serializer):

    password = serializers.CharField(
        max_length=64, min_length=8, required=True)
    password_confirmation = serializers.CharField(
        max_length=64, min_length=8, required=True)

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Password does not match.")
        password_validation.validate_password(data['password'])
        return data

    def save(self):
        password = self.validated_data['password']
        self.instance.set_password(password)
        self.instance.change_password()
        self.instance.save()


class StaffResetPasswordConfirm(PasswordSerializer):
    token = serializers.CharField(required=True)

    def validate_token(self, token):
        try:
            self.token_instance(token)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return token

    def token_instance(self, token):
        return EmailToken(token=token)

    def get_token_user(self):
        user_id = self.token_instance(
            self.validated_data['token']).payload['user_id']
        return get_object_or_404(Staff, **{'id': user_id, 'is_active': True})

    def save(self):
        self.instance = self.get_token_user()
        super().save()


class StaffChangePasswordSerializer(PasswordSerializer):

    old_password = serializers.CharField()

    def validate_old_password(self, value):

        invalid_password_conditions = (
            self.instance,
            not self.instance.check_password(value)
        )
        if all(invalid_password_conditions):
            msg = "Your old password was entered incorrectly. Please enter it again."
            raise serializers.ValidationError(msg)
        return value


class StaffResetPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)

    @classmethod
    def get_token(cls, user):
        return EmailToken.for_user(user)

    def validate_email(self, value):
        query = Staff.objects.filter(is_active=True).filter(
            profile__is_password_changed=True).filter(email__iexact=value)

        if not query:
            return ValidationError('There is no active user associated with this e-mail address or the password can not be changed')
        else:
            self.user = query[0]

    def save(self):
        token = self.get_token(self.user)
        # print(token)

        request_reset_password_email(self.user.email, str(token))
