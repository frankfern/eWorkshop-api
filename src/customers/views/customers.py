from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from ..models import Customer
from ..serializers import customers


class CustomerCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    model = Customer
    serializer_class = customers.CustomerCreateSerializer
    queryset = Customer.objects.all()


class CustomerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    model = Customer
    queryset = Customer.objects.all()
    serializer_class = customers.CustomerCreateSerializer
