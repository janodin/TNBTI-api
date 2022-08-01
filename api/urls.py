from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes, name='routes'),

    path('users/', views.getUsers, name='users'),
    #path('create-user/', views.createUser, name='create-user'),
    path('user/<str:pk>/', views.getUserDetail, name='user-detail'),
    path('update-user/<str:pk>/', views.updateUser, name='update-user'),
    path('delete-user/<str:pk>/', views.deleteUser, name='delete-user'),

    path('customers/', views.getCustomers, name='customers'),
    #path('create-customer/', views.createCustomer, name='create-customer'),
    path('customer/<str:pk>/', views.getCustomerDetail, name='customer-detail'),
    path('update-customer/<str:pk>/', views.updateCustomer, name='update-customer'),
    path('delete-customer/<str:pk>/', views.deleteCustomer, name='delete-customer'),
]
