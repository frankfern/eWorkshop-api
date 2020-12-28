from rest_framework import serializers


from ..models import FixService


class FixServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixService
        fields = '__all__'
