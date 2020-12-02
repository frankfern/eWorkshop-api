from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated


from ..models import FixService
from ..serializers import FixServiceSerializer


class FixServiceViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = FixServiceSerializer
    queryset = FixService.objects.all()
