from rest_framework import serializers
from .progress_serializer import ProgressListSerializer
from ..models import Client


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class ClientDetailSeriealizer(serializers.ModelSerializer):
    progress = ProgressListSerializer(source='client_progress', many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'progress']
