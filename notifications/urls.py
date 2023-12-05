from django.urls import path, include
from .views import GetNotification

urlpatterns = [
    path('notification/', GetNotification.as_view(), name='get_notification'),
]
