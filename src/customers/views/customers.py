from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated


from ..models import Customer
from ..serializers import customers


# class CustomerViewSet(mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.ListModelMixin,
#                       viewsets.GenericViewSet):

#     serializer_class = customers.CustomerCreateSerializer
#     queryset = Customer.objects.all()

class CustomerCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    model = Customer
    serializer_class = customers.CustomerCreateSerializer
    queryset = Customer.objects.all()


class CustomerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    model = Customer
    queryset = Customer.objects.all()
    serializer_class = customers.CustomerCreateSerializer
