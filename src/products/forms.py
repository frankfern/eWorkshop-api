from .models import Product
from base.forms import BaseForm

class ProductForm(BaseForm):

    class Meta:
        model = Product
        fields = '__all__'
