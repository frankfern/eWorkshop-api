from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from ..models import CustomerDevice
from ..serializers import devices


class DeviceListCreateView(ListCreateAPIView):
    model = CustomerDevice
    serializer_class = devices.DevicefSerializer
    queryset = CustomerDevice.objects.all()


class DeviceShowView(RetrieveUpdateAPIView):
    model = CustomerDevice
    serializer_class = devices.DevicefSerializer
    queryset = CustomerDevice.objects.all()
