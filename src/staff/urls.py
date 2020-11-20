from django.urls import path, re_path
from . import views


urlpatterns = [

    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),


    path("", views.StaffListView.as_view(), name="list"),
    path("create/", views.StaffCreateView.as_view(), name="create"),

    path("<str:pk>/", views.StaffDetailView.as_view(), name="detail"),
    path("<str:pk>/update/", views.StaffUpdateView.as_view(), name="update"),
    path("<str:pk>/delete/", views.StaffDeleteView.as_view(), name="delete"),
]
