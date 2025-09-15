from rest_framework import serializers
from ..models import Trail, Client
from .step_serializers import StepCreateSerializer


class TrailCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Trail
        fields = ['title', 'description']

class TrailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ['id', 'title', 'number_of_steps']
    
class TrailDetailSerializer(serializers.ModelSerializer):
    steps = StepCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Trail
        fields = ['id', 'title', 
                  'description', 'last_update', 
                  'number_of_steps', 'steps']
