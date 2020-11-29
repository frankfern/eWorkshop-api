from django.urls import path, re_path
from ..views import contacts


urlpatterns = [

    path("", contacts.ContactListCreateView.as_view(), name="list-create"),

]
