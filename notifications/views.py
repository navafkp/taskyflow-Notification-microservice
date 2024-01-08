from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from .serializers import getNotificationSerializer
from datetime import datetime, timezone
from django.http import JsonResponse


class GetNotification(APIView):
    """Get all notification and return based on the request"""
    def get(self, request):
        workspace = request.data.get('workspace')
        email = request.data.get('email')
        if email is not None:
            all_notification = Notification.objects.filter(userMail=email).order_by('-created_at')
        else:
            current_time_formatted = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f%z")
            all_notification = Notification.objects.filter(
                workspace=workspace,
                category = 'group',
            ) 
        if all_notification.exists():
            try:
                serializer = getNotificationSerializer(all_notification, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': "Someting went wrong, try refresh"})
        else:
            return Response({'message': 'No notifications found'})

# health check for docker
def healthcheck(request):
    return JsonResponse({'status': 'OK'})

