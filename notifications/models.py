from django.db import models

# Create your models here.

class Notification(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)
    workspace = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.type
