from .models import Device,Brand,Modelo
from base.forms import BaseForm

class DeviceForm(BaseForm):

    class Meta:
        model = Device
        fields = '__all__'


class BrandForm(BaseForm):

    class Meta:
        model = Brand
        fields = '__all__'


class ModeloForm(BaseForm):

    class Meta:
        model = Modelo
        fields = '__all__'
