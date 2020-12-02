from rest_framework import viewsets, mixins
from ..models import SparePartType
from ..serializers import sparepart_types


class SparePartTypeViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):

    serializer_class = sparepart_types.SparePartTypeSerializer
    queryset = SparePartType.objects.all()
