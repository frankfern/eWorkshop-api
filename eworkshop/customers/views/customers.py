from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated


from ..models import Customer
from ..serializers import customers


class CustomerViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = customers.CustomerCreateSerializer
    queryset = Customer.objects.all()
    ordering = ['created']
    ordering_fields = '__all__'
    filterset_fields = ['first_name', 'last_name', 'created', 'modified']
