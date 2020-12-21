from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from ..serializers import StaffChangePasswordSerializer, ListStaffSerializer, ShowStaffSerializer
from ..models import Profile

from utils.mixins import ListCreateSerializerMixin


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

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password('1234')
        user.save()
        Profile.objects.create(staff=user)

    @action(detail=True, methods=['put'], permission_classes=[IsAuthenticated])
    def change_password(self, request, pk=None):

        user = self.get_object()
        serializer = StaffChangePasswordSerializer(data=request.data)

        # check old password
        if not user.check_password(serializer.data.get('old_password')):
            return Response({
                "old_password": ["Wrong password"]
            }, status=status.HTTP_400_BAD_REQUEST)

        else:
            if serializer.is_valid():
                user.set_password(serializer.data['password'])
                user.save()

                profile = Profile.objects.get(staff_id=user.pk)
                profile.is_password_changed = True
                profile.save()

                return Response({'status': 'success',
                                 'code': status.HTTP_200_OK,
                                 'message': 'Password updated successfully'
                                 }, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
