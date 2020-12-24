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
    queryset = Contact.objects.all()

    def dispatch(self, request, *args, **kwargs):

        pk = kwargs['client_id']
        self.customer = get_object_or_404(Customer, id=pk)

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):

        return Contact.objects.filter(id=self.customer.id)
