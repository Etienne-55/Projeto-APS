from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('Product/', ProductList.as_view(), name='product-list'),
    path('Product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
