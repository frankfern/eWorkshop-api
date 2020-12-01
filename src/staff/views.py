from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Staff
from .serializers import *


class StaffCreateView(CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = CreateStaffSerializaer


class StaffListView(ListAPIView):
    serializer_class = BaseStaffSerializer
    queryset = Staff.objects.all()


class StaffShowView(RetrieveUpdateAPIView):
    serializer_class = ShowStaffSerializaer
    queryset = Staff.objects.all()
