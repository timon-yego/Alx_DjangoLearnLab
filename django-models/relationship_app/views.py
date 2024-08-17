from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'relationship_app/templates/relationship_app/list_books.html', {'books': books})

# Class-Based View: Display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/templates/relationship_app/library_detail.html'  # The template to be used
    context_object_name = 'library'  # The context variable name used in the template

# Login View (using Django's built-in view)
class LoginView(auth_views.LoginView):
    template_name = 'relationship_app/login.html'

# Logout View (using Django's built-in view)
class LogoutView(auth_views.LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration View (custom)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

