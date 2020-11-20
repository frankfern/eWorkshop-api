from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),

    path("create/", views.ProductCreateView.as_view(), name="create"),

    path("<str:pk>/", views.ProductDetailView.as_view(), name="detail"),
    path("<str:pk>/update/", views.ProductUpdateView.as_view(), name="update"),
    # path("<str:pk>/delete/", views.ProductDeleteView.as_view(), name="delete"),
]
