from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

from ..models import Contact, Customer
from ..serializers import contacts


class ContactViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = contacts.ContactSerializer
    ordering_fields = '__all__'
    filterset_fields = ['customer', 'created', 'modified']

    def dispatch(self, request, *args, **kwargs):

        self.customer_id = kwargs['client_id']
        self.customer = get_object_or_404(Customer, id=self.customer_id)

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):

        return Contact.objects.filter(id=self.customer_id)

    def create(self, request, *args, **kwargs):

        request.data['client'] = self.customer_id

        return super().create(request, *args, **kwargs)
