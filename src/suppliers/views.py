from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy


from base.decorators import DynamicOrderingDecorator, GetToPostDecorator, DynamicPaginateBy
from .models import Supplier
from .forms import SupplierForm


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "suppliers/create.html"
    form_class = SupplierForm
    success_url = reverse_lazy('Suppliers:list')


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = "suppliers/update.html"
    form_class = SupplierForm
    success_url = reverse_lazy('Suppliers:list')


@DynamicOrderingDecorator()
@DynamicPaginateBy()
class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers/list.html"
    context_object_name = 'Suppliers'


@GetToPostDecorator()
class SupplierDeleteView(DeleteView):
    model = Supplier
    queryset = Supplier.objects.all()
    success_url = reverse_lazy('Suppliers:list')


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "suppliers/detail.html"
