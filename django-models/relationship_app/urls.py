from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from .views import LoginView, LogoutView, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/templates/relationship_app/login.html'), name='login'),  # Login URL
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/templates/relationship_app/logout.html'), name='logout'),  # Logout URL
    path('register/', views.register, name='register'),  # Registration URL
    path('admin-view/', views.admin_view, name='admin_view'),  # URL for Admin view
    path('librarian-view/', views.librarian_view, name='librarian_view'),  # URL for Librarian view
    path('member-view/', views.member_view, name='member_view'),  # URL for Member view
    path('add-book/', views.add_book, name='add_book'),  # URL for adding a book
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),  # URL for editing a book
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),  # URL for deleting a book
]
