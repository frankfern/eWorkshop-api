from django.urls import path
from . import views


urlpatterns = [


    path("brand", views.BrandListView.as_view(), name="brand_list"),
    path("brand/create/", views.BrandCreateView.as_view(), name="brand_create"),
    path("brand/<str:pk>/update/", views.BrandUpdateView.as_view(), name="brand_update"), 
    

    path("device/", views.DeviceListView.as_view(), name="device_list"),
    path("device/create/", views.DeviceCreateView.as_view(), name="device_create"),
    path("device/<str:pk>/update/", views.DeviceUpdateView.as_view(), name="device_update"),
    
    path("modelo/", views.ModeloListView.as_view(), name="modelo_list"),
    path("modelo/create/", views.ModeloCreateView.as_view(), name="modelo_create"),
    path("modelo/<str:pk>/update/", views.ModeloUpdateView.as_view(), name="modelo_update"),
]
