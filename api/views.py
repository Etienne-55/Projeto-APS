from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        location = self.request.query_params.get('Location')
        if location is not None:
            queryset = queryset.filter(ProductLocation=location)
        return queryset
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = ProductSerializer
        queryset = Product.objects.all() 