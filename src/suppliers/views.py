from rest_framework import generics

from .models import Supplier
from .serializers import SupplierSerializer


class SupplierListCreateView(generics.ListCreateAPIView):
    model = Supplier
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierShowView(generics.RetrieveUpdateAPIView):
    model = Supplier
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
