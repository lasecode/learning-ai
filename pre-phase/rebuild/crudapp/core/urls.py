from django.urls import path
from .views import *

urlpatterns = [
    path('', view_contacts, name="home"),
    path('create_contact/', create_contact, name="create_contact"),
    path('search_contacts/', search_contacts, name="search_contacts"),
    path('update_contact/<int:pk>/', update_contact, name="update_contact"),
    path('delete_contact/<int:pk>/', delete_contact, name="delete_contact"),
]