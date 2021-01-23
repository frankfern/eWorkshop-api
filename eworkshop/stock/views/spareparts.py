from rest_framework import viewsets, mixins
from ..models import SparePart
from ..serializers import spareparts


class SparePartViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):

    serializer_class = spareparts.SparePartSerializer
    queryset = SparePart.objects.all()
    ordering_fields = '__all__'
    filterset_fields = ['created', 'modified', ]
