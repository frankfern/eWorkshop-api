from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from .models import Staff
from .serializers import CreateStaffSerializaer, ShowStaffSerializaer


class StaffListCreateView(ListCreateAPIView):
    model = Staff
    serializer_class = CreateStaffSerializaer
    queryset = Staff.objects.all()


class StaffShowView(RetrieveUpdateAPIView):
    model = Staff
    serializer_class = ShowStaffSerializaer
    queryset = Staff.objects.all()
