from rest_framework import viewsets, mixins


from ..models import CustomerDevice
from ..serializers import devices


class DeviceViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = devices.DevicefSerializer
    queryset = CustomerDevice.objects.all()
