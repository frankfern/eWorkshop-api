from rest_framework import serializers


from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['device_model', 'description', 'sn',
                  'supplier', 'condition', 'price', 'quantity', 'used_quantity',
                  'get_real_quantity']
