from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product, name='product-detail'),
    path('product-info/', views.product_info, name='product-info'),
    path('orders/', views.order_list, name='order-list'),    
]
