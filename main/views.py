from .models import Documents
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .serializers import DocSerializer
from rest_framework import viewsets
from .tasks import analyze_document_task
from rest_framework.response import Response

class DocumentViewset( viewsets.ModelViewSet):
    serializer_class= DocSerializer
    # queryset= Documents.objects.select_related('analysis').all()
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Documents.objects.filter(user=self.request.user).select_related('analysis').all()

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        analyze_document_task.delay(instance.id)

    @action(detail=True, methods=['post'])
    def reprocess(self, request, pk=None):
        document = self.get_object()

        analyze_document_task.delay(document.id)
        return Response({'status': 'Reprocessing started for document ' + str(document.id)})
