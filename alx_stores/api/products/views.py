from rest_framework import viewsets
from .serializers import ProductSerializer
from products.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
