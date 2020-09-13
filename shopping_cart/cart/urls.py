from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('cart', views.cart, name='cart'),
    path('create-product', views.create_product, name='create-product'),
    path('api/cart_products', views.cart_products),
    #TODO
    path('checkout', views.checkout_page, name="checkout"),
    
]