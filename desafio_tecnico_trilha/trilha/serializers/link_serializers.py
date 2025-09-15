from rest_framework import serializers
from ..models import Links

class LinkCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Links
        fields = ['title', 'link', 'step']

class LinkWithStepCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['title', 'link']

    def create(self, validated_data):
        step_id = self.context['step_id']
        return Links.objects.create(step_id=step_id, **validated_data)

class LinkListSerializer(serializers.ModelSerializer):
    step_title = serializers.CharField(source='step.title', read_only=True)
    class Meta:
        model = Links
        fields = ['id', 'link', 'step_title']
