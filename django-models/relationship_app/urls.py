from django.urls import path
from .views import list_books, LibraryDetailView
from .views import LoginView, LogoutView, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(), name='login'),  # Login URL
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout URL
    path('register/', register, name='register'),  # Registration URL
]
