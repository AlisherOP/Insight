from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documents
import time
from .tasks import analyze_document_task




@receiver(post_save, sender= Documents)
def trigger_ai_analysis(sender, instance, created, **kwargs):
    if created:
        analyze_document_task.delay(instance.id)
        # print(f"File {instance.pdf.name} received! Starting AI analysis...")
