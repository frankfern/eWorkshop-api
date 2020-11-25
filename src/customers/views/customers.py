from rest_framework import generics
from ..models import Customer
from ..serializers import customers


class CustomerCreateView(generics.CreateAPIView):
    model = Customer
    serializer_class = customers.CustomerSerializer


# class CustomerUpdateView(generics.UpdateAPIView):
#     model = Customer


class CustomerListView(generics.ListAPIView):

    model = Customer
    serializer_class = customers.CustomerSerializer
    queryset = Customer.objects.all()
    context_object_name = 'Customers'


# class CustomerDeleteView(generics.DestroyAPIView):
#     pass


# class CustomerDetailView(generics.RetrieveAPIView):
#     model = Customer
