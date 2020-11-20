from .models import Provider
from base.forms import BaseForm

class ProviderForm(BaseForm):

    class Meta:
        model = Provider
        fields = '__all__'
