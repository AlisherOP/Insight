from django.db import models
from django.contrib.auth.models import User


class Documents(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pdfs')
    pdf = models.FileField(upload_to='pdfs/%Y/%m/%d/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # Status tracks the Celery background task
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')



    def __str__(self):
        return self.user.username
    

class Analysis(models.Model):
    document= models.OneToOneField(
        Documents, on_delete=models.CASCADE, related_name='analysis'
        )
    summary = models.TextField()
    sentiment= models.CharField(max_length=50)
    
    
