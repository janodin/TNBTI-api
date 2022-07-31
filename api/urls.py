from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes, name='routes'),
    path('users/', views.getUsers),
    path('customers/', views.getCustomers),
]
