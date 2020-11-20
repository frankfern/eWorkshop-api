from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy, reverse

from django.views.generic import FormView, DeleteView, UpdateView, CreateView, DetailView, ListView
from django.contrib.auth import views as auth_views


from .forms import CreateUserForm, ChangeUserForm
from .models import Staff


class StaffCreateView(CreateView):
    model = Staff
    template_name = "staff/create.html"
    form_class = CreateUserForm
    success_url = reverse_lazy('staff:list')


class StaffListView(ListView):
    model = Staff
    template_name = "staff/list.html"
    context_object_name = 'staff'
    ordering = ('-first_name',)
    paginate_by = 10


class StaffDetailView(DetailView):
    model = Staff
    template_name = "staff/detail.html"
    context_object_name = 'staff'


class StaffUpdateView(UpdateView):
    model = Staff
    template_name = "staff/update.html"
    form_class = ChangeUserForm

    def get_success_url(self):
        """Return to user's profile """
        id = self.object.id
        return reverse('staff:detail', kwargs={'pk': id})


class StaffDeleteView(DeleteView):
    model = Staff
    queryset = Staff.objects.all()
    success_url = reverse_lazy('staff:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class Login(auth_views.LoginView):
    """Login """
    template_name = 'staff/login.html'


class Logout(auth_views.LogoutView):
    """Logout """
