from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from base.decorators import DynamicOrderingDecorator, GetToPostDecorator, DynamicPaginateBy
from .models import Customer
from .forms import CustomerForm


class CustomerCreateView(CreateView):
    model = Customer
    template_name = "Customers/create.html"
    form_class = CustomerForm
    success_url = reverse_lazy('Customers:list')


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "Customers/update.html"
    form_class = CustomerForm
    success_url = reverse_lazy('Customers:list')


@DynamicOrderingDecorator()
@DynamicPaginateBy()
class CustomerListView(ListView):
    model = Customer
    template_name = "Customers/list.html"
    context_object_name = 'Customers'


@GetToPostDecorator()
class CustomerDeleteView(DeleteView):
    model = Customer
    queryset = Customer.objects.all()
    success_url = reverse_lazy('Customers:list')


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "Customers/detail.html"
