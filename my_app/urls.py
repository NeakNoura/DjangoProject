from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # The home page
    path('product/', views.product, name='product'),  # Product list page
    path('customer/<str:pk>/', views.customer, name='customer'),  # Customer details page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('create_order/', views.createOrder, name='create_order'),  # Create order page
    path('create-customer/', views.createCustomer, name='create_customer'),  # Create customer page
    path('update_customer/<str:pk>/', views.updateCustomer, name='update_customer'),  # Update customer page
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),  # Update order page
    path('delete_customer/<str:pk>/', views.deleteCustomer, name='delete_customer'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

]
