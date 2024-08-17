from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'relationship_app/templates/relationship_app/list_books.html', {'books': books})

# Class-Based View: Display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/templates/relationship_app/library_detail.html'  # The template to be used
    context_object_name = 'library'  # The context variable name used in the template

