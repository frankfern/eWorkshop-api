from rest_framework import serializers


from ..models import SparePart


class SparePartSerializer(serializers.ModelSerializer):
    model = SparePart
    fields = '__all__'
