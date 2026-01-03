from api.serializers import ProductSerializer, OrderSerializer, OrderItemSerializer, ProductInfoSerializer
from api.models import Product, Order, OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import models
from rest_framework import generics




class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(stock__gt=0)
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductInfoAPIView(generics.GenericAPIView):
    serializer_class = ProductInfoSerializer

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        data = {
            'products': products,
            'count': products.count(),
            'max_price': products.aggregate(models.Max('price'))['price__max'] or 0,
        }
        serializer = self.get_serializer(data)
        return Response(serializer.data)