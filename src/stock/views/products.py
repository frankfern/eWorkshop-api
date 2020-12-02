from rest_framework import viewsets, mixins
from ..models import Product
from ..serializers import products


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = products.ProductSerializer
    queryset = Product.objects.all()
