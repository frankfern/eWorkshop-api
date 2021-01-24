from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from ..serializers import StaffChangePasswordSerializer, ListStaffSerializer, ShowStaffSerializer
from eworkshop.utils.viewmixins import ListCreateSerializerMixin


Staff = get_user_model()


class StaffViewSet(ListCreateSerializerMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = Staff.objects.all()
    list_serializer_class = ListStaffSerializer
    write_serializer_class = ShowStaffSerializer
    lookup_field = 'username'
    ordering_fields = '__all__'
    ordering = ['created']
    filterset_fields = ['created', 'modified', ]

    @action(detail=False, methods=['put'], permission_classes=[IsAuthenticated])
    def change_password(self, request, *args, **kwargs):

        serializer = StaffChangePasswordSerializer(
            data=request.data,
            instance=request.user,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data={'status': 'success',
                              'code': status.HTTP_200_OK,
                              'message': 'Password updated successfully'
                              }, status=status.HTTP_200_OK)
