from rest_framework import serializers

from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    is_password_changed = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ('picture', 'is_password_changed')
