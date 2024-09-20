from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets,permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework import status, generics

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the current user
        user = request.user

        # Get the users the current user is following
        following_users = user.following.all()

        # Filter posts from the users that the current user is following and order by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)

        # Return the serialized data
        return Response(serializer.data)

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Use get_object_or_404 to fetch the Post by primary key (pk)
        post = generics.get_object_or_404(Post, pk=pk)

        # Create or retrieve the Like object
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # If a like was created, send a notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )
            return Response({"message": "Post liked and notification sent."}, status=status.HTTP_201_CREATED)
        else:
            # If the user has already liked the post
            return Response({"message": "You have already liked this post."}, status=status.HTTP_200_OK)
        

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Fetch the post object, or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        try:
            # Try to retrieve the Like object
            like = Like.objects.get(user=request.user, post=post)
            # If found, delete it to unlike the post
            like.delete()
            return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            # If the Like object doesn't exist, return an error
            return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
