from rest_framework import generics

from ..models import Contact
from ..serializers import contacts


class ContactListCreateView(generics.ListCreateAPIView):
    model = Contact
    serializer_class = contacts.ContactSerializer
    queryset = Contact.objects.all()
