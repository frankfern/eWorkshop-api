from eworkshop.stock.models import products
from rest_framework import serializers

from ..models import ServiceProduct


class ServiceProductSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source="product.id")

    class Meta:
        model = ServiceProduct
        fields = ['product', 'quantity_bought', 'service']
