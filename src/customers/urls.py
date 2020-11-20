from django.urls import path, re_path
from . import views


urlpatterns = [

    path("", views.CustomerListView.as_view(), name="list"),

    path("create/", views.CustomerCreateView.as_view(), name="create"),

    path("<str:pk>/", views.CustomerDetailView.as_view(), name="detail"),
    path("<str:pk>/update/", views.CustomerUpdateView.as_view(), name="update"),
    path("<str:pk>/delete/", views.CustomerDeleteView.as_view(), name="delete"),
]
