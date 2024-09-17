# contacts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('detail/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('search/', views.search_contacts, name='search_contacts'),
]
