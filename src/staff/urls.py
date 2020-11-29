from django.urls import path, re_path

from . import views


urlpatterns = [


    path("", views.StaffListCreateView.as_view(), name="list"),

    path("<str:pk>/", views.StaffShowView.as_view(), name="detail"),
]
