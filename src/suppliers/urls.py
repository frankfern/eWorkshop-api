from django.urls import path
from . import views


urlpatterns = [
    path("", views.SupplierListCreateView.as_view(), name="list"),

    path("<str:pk>/", views.SupplierShowView.as_view(), name="detail"),
]
