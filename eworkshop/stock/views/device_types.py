from rest_framework import viewsets, mixins
from ..models import DeviceType
from ..serializers import device_types


class DeviceTypeViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = device_types.DeviceTypeSerializer
    queryset = DeviceType.objects.all()
