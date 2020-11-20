from django.urls import path
from . import views


urlpatterns = [
    path("", views.SupplierListView.as_view(), name="list"),

    path("create/", views.SupplierCreateView.as_view(), name="create"),

    path("<str:pk>/", views.SupplierDetailView.as_view(), name="detail"),
    path("<str:pk>/update/", views.SupplierUpdateView.as_view(), name="update"),
    path("<str:pk>/delete/", views.SupplierDeleteView.as_view(), name="delete"),
]
