from rest_framework import viewsets, mixins, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


from ..models import ServiceProduct, SellService
from ..serializers import ServiceProductSerializer


class ServiceProductViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):

    serializer_class = ServiceProductSerializer
    queryset = ServiceProduct.objects.all()

    # def dispatch(self, request, *args, **kwargs):

    #     service_id = kwargs['service_id']
    #     self.service = get_object_or_404(SellService, pk=service_id)
    #     return super().dispatch(request, *args, **kwargs)

    # def get_queryset(self):
    #     return ServiceProduct.objects.filter(
    #         service=self.service,
    #     )

    # def create(self, request, *args, **kwargs):
    #     serializer = AddMemberSerializer(
    #         data=request.data,
    #         context={'service': self.service, 'request': request}
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     product = serializer.save()

    #     data = self.get_serializer(product).data
    #     return Response(data, status=status.HTTP_201_CREATED)
