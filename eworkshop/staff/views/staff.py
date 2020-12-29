from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser


from django.contrib.auth import get_user_model

# from staff.serializers import profile

from ..serializers import StaffChangePasswordSerializer, ListStaffSerializer, ShowStaffSerializer
from ..serializers import profile as profile_serializer
from ..models import Profile

from eworkshop.utils.mixins import ListCreateSerializerMixin


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

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password('1234')
        user.save()
        Profile.objects.create(staff=user)

    @action(detail=True, methods=['put', 'patch'], parser_classes=(MultiPartParser, FormParser))
    def profile(self, request, *args, **kwargs):
        """Update Profile Data"""
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = profile_serializer.ProfileSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = ShowStaffSerializer(user).data
        return Response(data)

    @action(detail=True, methods=['put'], permission_classes=[IsAuthenticated])
    def change_password(self, request, *args, **kwargs):

        user = self.get_object()
        serializer = StaffChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # check old password
        if not user.check_password(serializer.data.get('old_password')):
            return Response({
                "old_password": ["Wrong password"]
            }, status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer.is_valid(raise_exception=True)
            user.set_password(serializer.data['password'])
            user.save()

            profile = Profile.objects.get(staff_id=user.pk)
            profile.is_password_changed = True
            profile.save()

            return Response({'status': 'success',
                             'code': status.HTTP_200_OK,
                             'message': 'Password updated successfully'
                             }, status=status.HTTP_200_OK)
