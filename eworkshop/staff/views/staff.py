from decimal import Context
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser


from django.contrib.auth import get_user_model


from ..serializers import StaffChangePasswordSerializer, ListStaffSerializer, ShowStaffSerializer
from ..serializers import profile as profile_serializer
from ..models import Profile

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

    @action(detail=False, methods=['put', 'patch'], parser_classes=(MultiPartParser, FormParser))
    def profile(self, request, *args, **kwargs):
        """Update Profile Data"""
        user = request.user
        partial = request.method == 'PATCH'

        serializer = profile_serializer.ProfileSerializer(
            user.profile,
            data=request.data,
            partial=partial
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = ShowStaffSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)

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
