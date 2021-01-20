from django.db import transaction
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from eworkshop.stock.models import Product

from ..models import SellService, ServiceProduct
from .service_product import ServiceProductSerializer


class SellServiceSerializer(serializers.ModelSerializer):
    products = ServiceProductSerializer(
        many=True, source='serviceproduct_set')

    price = serializers.ReadOnlyField()

    class Meta:
        model = SellService
        fields = ['id', 'customer', 'worker',
                  'products', 'price', 'discount',
                  'description', 'has_warranty',
                  'warrantyoff']

    @transaction.atomic
    def update(self, instance, validated_data):
        ServiceProduct.objects.filter(service=instance).delete()
        products = self.initial_data.get("products")

        for product in products:
            id = product.get("id")
            quantity = product.get("quantity_bought")
            new_product = get_object_or_404(Product, id=id)
            ServiceProduct.objects.create(service=instance, product=new_product,
                                          quantity_bought=quantity)

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

    @transaction.atomic
    def create(self, validated_data):
        """
        docstring
        """
        sell_service = SellService.objects.create(**validated_data)
        if "products" in self.initial_data:
            products = self.initial_data.get("products")
            for product in products:
                id = product.get("id")
                quantity = product.get("quantity_bought")
                product_instance = get_object_or_404(Product, id=id)
                ServiceProduct.objects.create(service=sell_service, product=product_instance,
                                              quantity_bought=quantity)
        sell_service.save()
        return sell_service

    def validate_products(self, validated_data):
        if not "products" in self.initial_data:
            raise serializers.ValidationError(
                detail="You must send at least one product")
