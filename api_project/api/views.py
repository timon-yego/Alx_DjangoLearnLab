from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import viewsets  # Import viewsets from DRF
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer

# Define the BookViewSet using ModelViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Set the queryset to all Book instances
    serializer_class = BookSerializer  # Set the serializer class to BookSerializer

