from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from rest_framework import generics
from base.decorators import DynamicOrderingDecorator, GetToPostDecorator, DynamicPaginateBy
from .models import Customer
from .forms import CustomerForm


class CustomerCreateView(CreateView):
    model = Customer


class CustomerUpdateView(UpdateView):
    model = Customer


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
