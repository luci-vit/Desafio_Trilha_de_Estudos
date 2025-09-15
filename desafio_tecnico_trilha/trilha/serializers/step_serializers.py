from rest_framework import serializers
from .link_serializers import LinkCreateSerializer
from .attachments_serializers import AttachmentCreateSerializer
from ..models import Step

class StepCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['title', 'description', 'order', 'trail']

class StepWithTrailCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Step
        fields = ['title', 'description', 'order']

    def create(self, validated_data):
      trail_id = self.context['trail_id']
      return Step.objects.create(trail_id=trail_id, **validated_data)

class StepListSerializer(serializers.ModelSerializer):
    links = LinkCreateSerializer(many=True, read_only=True)
    attachments = AttachmentCreateSerializer(many=True, read_only=True)
    trail_title = serializers.CharField(source='trail.title', read_only=True)
    class Meta: 
        model = Step
        fields = ['trail_title', 'title', 'description', 'links', 'attachments'] 

class StepDetailSerializer(serializers.ModelSerializer):
    links = LinkCreateSerializer(many=True, read_only=True)
    attachments = AttachmentCreateSerializer(many=True, read_only=True)
    trail_title = serializers.CharField(source='trail.title', read_only=True)
    class Meta:
        model = Step
        fields = ['trail_title', 'title', 'description', 'order', 'trail', 'links', 'attachments']
