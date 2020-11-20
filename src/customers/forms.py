from base.forms import BaseForm
from .models import Client


class ClientForm(BaseForm):

    class Meta:
        model = Client
        fields = '__all__'
