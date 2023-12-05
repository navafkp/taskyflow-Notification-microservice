from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from .serializers import getNotificationSerializer

class GetNotification(APIView):
    def get(self, request):
        print("hi")
        print(request.data.get('workspace'))
        workspace = request.data.get('workspace')
        all_notification = Notification.objects.filter(workspace=workspace)
        try:
            serializer = getNotificationSerializer(all_notification, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'error': "Someting went wrong, try refresh"})
 
        