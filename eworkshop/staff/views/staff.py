from eworkshop.staff.serializers.staff import StaffResetPasswordSerializer
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import get_user_model

from ..serializers import StaffChangePasswordSerializer, ListStaffSerializer, ShowStaffSerializer, StaffResetPasswordConfirm
from eworkshop.utils.viewmixins import ListCreateSerializerMixin
from eworkshop.utils.utils import handle_serializers, fresponse


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

        handle_serializers(
            StaffChangePasswordSerializer,
            instance=request.user,
            data=request.data,
        )
        return fresponse('Password updated successfully')

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_name='password_reset')
    def password_reset(self, request, *args, **kwargs):
        handle_serializers(
            StaffResetPasswordSerializer,
            data=request.data,
        )
        return fresponse('Mail sended')

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def reset_password_confirm(self, request, *args, **kwargs):
        handle_serializers(
            StaffResetPasswordConfirm,
            data=request.data,
        )
        return fresponse('Password Changed Succesfully')
