from rest_framework import serializers
from ..models import ClientProgress, Step

class ProgressWithClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProgress
        fields = ['trail']

    def create(self, validated_data):
        client_id = self.context['client_id']
        trail = validated_data['trail']

        first_step = Step.objects.filter(trail=trail).order_by('order').first()
        if not first_step:
            raise serializers.ValidationError(
                {'trail': 'Essa trilha não possui nenhuma etapa para iniciar.'}
            )
        
        progress, created = ClientProgress.objects.get_or_create(
            client_id=client_id,
            trail=trail,
            step=first_step
        )
        
        return progress


class ProgressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProgress
        fields = ['completed']

class ProgressListSerializer(serializers.ModelSerializer):
    step = serializers.CharField(source='step.title', read_only=True)
    trail = serializers.CharField(source='trail.title', read_only=True)
    
    class Meta:
        model = ClientProgress
        fields = ['trail', 'step', 'completed']

class ProgresDetailListSerializer(serializers.ModelSerializer):
    step = serializers.CharField(source='step.title', read_only=True)
    trail = serializers.CharField(source='trail.title', read_only=True)
    client = serializers.CharField(source='client.name', read_only=True)
    
    class Meta:
        model = ClientProgress
        fields = ['id', 'client', 'trail', 'step', 'completed']