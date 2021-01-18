from rest_framework import serializers


from ..models import SellService


class SellServiceSerializer(serializers.ModelSerializer):
    products = serializers.MultipleChoiceField(
        queryset=SellService.objects.all())

    class Meta:
        model = SellService
        fields = ['customer', 'worker', 'products', 'price']
