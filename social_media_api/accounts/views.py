from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # After the object is created, create or get the token
        token, created = Token.objects.get_or_create(user=self.object)
        return Response({'token': token.key})

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"})

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"})