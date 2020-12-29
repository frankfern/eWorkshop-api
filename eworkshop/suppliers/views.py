
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins

from .models import Supplier
from .serializers import SupplierSerializer


class CustomerViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
