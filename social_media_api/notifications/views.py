from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification


# Create your views here.
class UnreadNotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        notifications = user.notifications.filter(read=False).order_by('-timestamp')
        data = [
            {
                "actor": notification.actor.username,
                "verb": notification.verb,
                "timestamp": notification.timestamp,
                "target": str(notification.target),
            }
            for notification in notifications
        ]
        return Response(data, status=200)