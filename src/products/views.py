from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy


from base.decorators import DynamicOrderingDecorator, GetToPostDecorator, DynamicPaginateBy
from .models import Product
from .forms import ProductForm


class ProductCreateView(CreateView):
    model = Product
    template_name = "products/create.html"
    form_class = ProductForm
    success_url = reverse_lazy('products:list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/update.html"
    form_class = ProductForm
    success_url = reverse_lazy('products:list')


@DynamicOrderingDecorator()
@DynamicPaginateBy()
class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
