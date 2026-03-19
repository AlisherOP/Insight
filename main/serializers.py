from rest_framework import serializers
from .models import Documents, Analysis



class AnalSerializer(serializers.ModelSerializer):
    class Meta:
        model= Analysis
        fields = ['id', 'summary', 'sentiment']


class DocSerializer(serializers.ModelSerializer):
    analysis= AnalSerializer(read_only=True)
    user= serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Documents
        fields = ['id', 'user', 'pdf', 'status', 'uploaded_at', 'analysis']
        read_only_fields = ['user', 'status']
