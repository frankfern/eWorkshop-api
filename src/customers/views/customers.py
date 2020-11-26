from rest_framework import generics

from ..models import Customer
from ..serializers import customers


class CustomerCreateListView(generics.ListCreateAPIView):
    model = Customer
    serializer_class = customers.CustomerCreateSerializer
    queryset = Customer.objects.all()


class CustomerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    model = Customer
    queryset = Customer.objects.all()
    serializer_class = customers.CustomerCreateSerializer
