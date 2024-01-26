from django.urls import path

from .views import index, products

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
]
