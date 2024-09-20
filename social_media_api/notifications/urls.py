from django.urls import path
from .views import UnreadNotificationsView

urlpatterns = [
    path('', UnreadNotificationsView.as_view(), name='unread_notifications'),
]