from django.contrib import admin
from django.urls import path, include
from notifications.views import healthcheck

urlpatterns = [
    path('healthcheck/', healthcheck),
    path('admin/', admin.site.urls),
    path('api/', include('notifications.urls')),
]
