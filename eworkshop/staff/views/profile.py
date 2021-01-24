from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser


from eworkshop.utils.viewmixins import RetrieveUpdateAPIView
from ..serializers import ShowStaffSerializer, profile as profile_serializer
from ..models import Profile


class ProfileViews(RetrieveUpdateAPIView, generics.RetrieveUpdateAPIView):

    queryset = Profile.objects.all()
    write_serializer_class = profile_serializer.ProfileSerializer
    list_serializer_class = ShowStaffSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_object(self):

        if self.request.method == 'GET':
            instance = self.request.user
        else:
            instance = self.request.user.profile

        return instance
