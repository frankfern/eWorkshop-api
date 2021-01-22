from eworkshop.stock.models import products
from rest_framework import serializers

from ..models import FixSparepart


class FixSparepartSerializer(serializers.ModelSerializer):
    sparepart = serializers.ReadOnlyField(source="sparepart.id")
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FixSparepart
        fields = ['sparepart', 'quantity', 'service']

    def create(self, validated_data):

        service = self.context['service']
        sparepart = validated_data['sparepart']
        quantity = validated_data['quantity']

        fixsparepart = FixSparepart.objects.create_or_update_quantity(
            service=service,
            sparepart=sparepart,
            quantity=quantity
        )
        return fixsparepart
