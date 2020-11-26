from django.urls import path, re_path
from ..views import customers


urlpatterns = [

    path("", customers.CustomerCreateListView.as_view(), name="list-create"),

    path("<str:pk>/", customers.CustomerRetrieveUpdateView.as_view(), name="detail"),
]
