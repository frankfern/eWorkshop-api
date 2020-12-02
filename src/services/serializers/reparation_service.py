from rest_framework import serializers


from ..models import FixService


class FixServiceSerializer(serializers.ModelSerializer):
    model = FixService
    fields = '__all__'
