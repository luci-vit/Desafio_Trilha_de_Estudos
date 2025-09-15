from rest_framework import serializers, viewsets
from drf_spectacular.utils import extend_schema
from ..models import Attachments

# Serializer para criação e atualização
class AttachmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachments
        fields = ['name', 'phone', 'email', 'video_duration', 'link']

# Serializer para criação passando algum contexto extra (opcional)
class AttachmentWithStepCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachments
        fields = ['name', 'phone', 'email', 'video_duration', 'link']

    def create(self, validated_data):
        step_id = self.context['step_id']
        return Attachments.objects.create(step_id=step_id, **validated_data)


# Serializer para listagem
class AttachmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachments
        fields = ['id', 'name', 'phone', 'email', 'video_duration', 'link']
