from django.urls import path, re_path
from ..views import devices


urlpatterns = [

    path("", devices.DeviceListCreateView.as_view(), name="list-create"),

    path("<str:pk>/", devices.DeviceShowView.as_view(), name="detail"),

]
