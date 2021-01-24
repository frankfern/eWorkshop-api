from rest_framework import viewsets, mixins
from ..models import DeviceModel
from ..serializers import device_models


class DeviceModelViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):

    serializer_class = device_models.DeviceModelSerializer
    queryset = DeviceModel.objects.all()
    ordering_fields = '__all__'
    ordering = ['created']
    filterset_fields = ['created', 'modified', ]
