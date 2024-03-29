from rest_framework import viewsets, mixins
from ..models import Brand
from ..serializers import brands


class BrandViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = brands.BrandSerializer
    queryset = Brand.objects.all()
    ordering_fields = '__all__'
    filterset_fields = ['created', 'modified', ]
    ordering = ['created']
