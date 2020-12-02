from rest_framework import mixins
from rest_framework import viewsets

from ..models import Contact
from ..serializers import contacts


class ContactViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = contacts.ContactSerializer
    queryset = Contact.objects.all()
