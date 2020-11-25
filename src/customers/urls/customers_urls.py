from django.urls import path, re_path
from ..views import customers


urlpatterns = [

    path("", customers.CustomerCreateView.as_view(), name="create"),

    path("", customers.CustomerListView.as_view(), name="list"),

    # path("<str:pk>/", views.CustomerDetailView.as_view(), name="detail"),
    # path("<str:pk>/", views.CustomerUpdateView.as_view(), name="update"),
    # path("<str:pk>/", views.CustomerDeleteView.as_view(), name="delete"),
]
