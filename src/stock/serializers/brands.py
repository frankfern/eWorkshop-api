from rest_framework import serializers


from ..models import Brand


class BrandSerializer(serializers.ModelSerializer):
    model = Brand
    fields = '__all__'
