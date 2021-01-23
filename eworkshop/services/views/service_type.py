from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated


from ..models import ServiceType
from ..serializers import ServiceTypeSerializer


class ServiceTypeViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):

    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()
    ordering_fields = '__all__'
    filterset_fields = ['created', 'modified', ]
