from django.urls import path, re_path

from . import views


urlpatterns = [

    path('register/', views.StaffCreateView.as_view(), name='create'),
    path("", views.StaffListView.as_view(), name="list"),

    path("<str:pk>/", views.StaffShowView.as_view(), name="detail"),
]
