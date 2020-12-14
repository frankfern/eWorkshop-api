from rest_framework import serializers


from ..models import SellService


class SellServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellService
        fields = '__all__'
