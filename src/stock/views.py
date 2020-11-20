from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy

from base.decorators import DynamicOrderingDecorator, DynamicPaginateBy

from .models import Brand,Device,Modelo
from .forms import BrandForm,DeviceForm,ModeloForm


class BrandCreateView(CreateView):
    model = Brand
    # template_name = "clients/create.html"
    form_class = BrandForm
    # success_url = reverse_lazy('clients:list')


class BrandUpdateView(UpdateView):
    model = Brand
    # template_name = "clients/update.html"
    form_class = BrandForm
    # success_url = reverse_lazy('clients:list')


@DynamicOrderingDecorator()
@DynamicPaginateBy()
class BrandListView(ListView):
    model = Brand
    # template_name = "clients/list.html"
    # context_object_name = 'brands'


class DeviceCreateView(CreateView):
    model = Device
    # template_name = "clients/create.html"
    form_class = DeviceForm
    # success_url = reverse_lazy('clients:list')


class DeviceUpdateView(UpdateView):
    model = Device
    # template_name = "clients/update.html"
    form_class = DeviceForm
    # success_url = reverse_lazy('clients:list')


@DynamicOrderingDecorator()
@DynamicPaginateBy()
class DeviceListView(ListView):
    model = Device
    # template_name = "clients/list.html"
    # context_object_name = 'devices'




class ModeloCreateView(CreateView):
    model = Modelo
    # template_name = "clients/create.html"
    form_class = ModeloForm
    # success_url = reverse_lazy('clients:list')


class ModeloUpdateView(UpdateView):
    model = Modelo
    # template_name = "clients/update.html"
    form_class = ModeloForm
    # success_url = reverse_lazy('clients:list')


@DynamicOrderingDecorator()
@DynamicPaginateBy()
class ModeloListView(ListView):
    model = Modelo
    # template_name = "clients/list.html"
    # context_object_name = 'modelos'
