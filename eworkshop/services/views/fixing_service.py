from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated


from ..models import FixService
from ..serializers import FixServiceSerializer


class FixServiceViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = FixServiceSerializer
    queryset = FixService.objects.all()
    ordering_fields = '__all__'
    ordering = ['created']
    filterset_fields = ['clients_device', 'service_type',
                        'created', 'modified', 'status']
