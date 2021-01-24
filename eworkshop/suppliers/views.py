
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins

from .models import Supplier
from .serializers import SupplierSerializer


class SupplierViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    ordering_fields = '__all__'
    ordering = ['created']
    filterset_fields = ['first_name', 'last_name', 'created', 'modified']
