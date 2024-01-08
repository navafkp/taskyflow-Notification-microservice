from django.db import models
from datetime import timedelta
# Create your models here.

class Notification(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)
    workspace = models.CharField(max_length=50)
    userMail = models.CharField(null=True, blank=True, max_length=200)
    is_read = models.BooleanField(default=False)
    category = models.CharField(max_length=100, default='group')
    expiry_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.type
    def category_set(self):
        if self.category == 'group':
            self.expiry_time = self.created_at + timedelta(hours=1)
            self.save()