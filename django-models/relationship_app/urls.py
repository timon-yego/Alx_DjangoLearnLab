from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from .views import LoginView, LogoutView, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.LoginView.as_view(), name='login'),  # Login URL
    path('logout/', views.LogoutView.as_view(), name='logout'),  # Logout URL
    path('register/', views.register, name='register'),  # Registration URL
]
