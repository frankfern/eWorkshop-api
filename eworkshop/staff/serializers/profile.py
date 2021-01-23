from rest_framework import serializers

from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    is_password_changed = serializers.ReadOnlyField()
    picture = serializers.ImageField(
        max_length=None, allow_empty_file=True, allow_null=True, required=False)

    class Meta:
        model = Profile
        fields = ('picture', 'is_password_changed')

    def update(self, instance, validated_data):

        if validated_data['picture'] is None:
            instance.picture = "/images/avatar.jpg"
        instance.save()
        return instance
