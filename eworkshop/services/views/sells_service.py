from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated


from ..models import SellService
from ..serializers.sells_service import SellServiceSerializer


class SellServiceViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):

    serializer_class = SellServiceSerializer
    queryset = SellService.objects.all()
    ordering_fields = '__all__'
    filterset_fields = ['created', 'modified', ]
