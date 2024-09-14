from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post_list'),                  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # View post details
    path('post/new/', PostCreateView.as_view(), name='post_create'),       # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'), # Update a post (the missing URL)
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'), # Delete a post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]