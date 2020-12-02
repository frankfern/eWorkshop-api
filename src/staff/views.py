from rest_framework import viewsets, mixins

from django.contrib.auth import get_user_model

from .serializers import *
from .mixins import ShowCreateSerializerMixin


Staff = get_user_model()


class StaffViewSet(ShowCreateSerializerMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = Staff.objects.all()
    list_serializer_class = ListStaffSerializer
    write_serializer_class = CreateStaffSerializaer

    # def change_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = StaffPasswordSerializer(data=request.data)
