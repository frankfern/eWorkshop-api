from rest_framework import serializers

from ..models import ServiceProduct


class ServiceProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceProduct
        fields = ['product', 'quantity_bought', 'service']
