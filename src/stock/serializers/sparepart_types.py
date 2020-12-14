from rest_framework import serializers


from ..models import SparePartType


class SparePartTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePartType
        fields = '__all__'
