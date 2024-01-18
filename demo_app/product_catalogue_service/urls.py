from django.urls import path
from .views import *

urlpatterns = [
    path('products/add', create_products, name='add product'),
    path('products', products, name='list products'),
    path('product', product_details, name='product details'),
]
