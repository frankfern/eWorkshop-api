from rest_framework import viewsets, mixins, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ..models import FixSparepart, FixService
from ..serializers.fix_sparepart import FixSparepartSerializer


class FixSparepartViewset(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):

    serializer_class = FixSparepartSerializer
    ordering_fields = '__all__'
    filterset_fields = ['fix', 'sparepart',
                        'created', 'modified']

    def dispatch(self, request, *args, **kwargs):
        service_id = kwargs['service_id']
        self.service = get_object_or_404(FixService, pk=service_id)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return FixSparepart.objects.filter(service=self.service)

    def get_object(self):
        return get_object_or_404(
            FixSparepart,
            service=self.service,
            sparepart=self.kwargs['pk']
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={
                'service': self.service,
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
