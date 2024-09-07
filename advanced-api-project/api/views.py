from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
import datetime
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters  # Import django_filters

# Create your views here.
# ListView to retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only access for unauthenticated users 

     # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Set up filter fields (filter by title, author, publication_year)
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Enable search functionality (search by title and author name)
    search_fields = ['title', 'author__name']
    
    # Enable ordering (order by title, publication_year)
    ordering_fields = ['title', 'publication_year']


# DetailView to retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only access for unauthenticated users

# CreateView to add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        # Ensure the publication year is not in the future
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year > datetime.date.today().year:
            raise ValidationError("Publication year cannot be in the future.")

# UpdateView to modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update

    def perform_update(self, serializer):
        # Ensure the publication year is not in the future
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year > datetime.date.today().year:
            raise ValidationError("Publication year cannot be in the future.")

# DeleteView to remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete