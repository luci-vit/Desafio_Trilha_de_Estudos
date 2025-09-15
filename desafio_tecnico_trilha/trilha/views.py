from django.db.models import Count 
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from .models import Trail, Step, Links, Client
from .serializers import *
from drf_spectacular.utils import extend_schema, OpenApiParameter

# # Essa classe é responsável por responder as requisições das urls: trails/ e trails/<trail_pk>
# # Ele implementa para o endPoint "trails/" os métodos POST e GET e para o endPoint trails/<trail_pk> ele implementa o DELET e PATCH
# class TrailViewSet(viewsets.ModelViewSet):
@extend_schema(tags=['Trilhas'])
class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TrailListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return TrailCreateSerializer
        return TrailDetailSerializer

@extend_schema(tags=['Clients'])
class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ClientListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ClientCreateSerializer
        return ClientDetailSeriealizer

@extend_schema(tags=['Client Progress'])
class ClientProgressWithClientViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProgressListSerializer
        elif self.action in ['create']:
            return ProgressWithClientCreateSerializer
        elif self.action in ['partial_update']:
            return ProgressUpdateSerializer
        return ProgresDetailListSerializer
    
    def get_serializer_context(self):
        return {'client_id': self.kwargs['client_pk']}
    
    def get_queryset(self):
        client_id = self.kwargs['client_pk']
        return ClientProgress.objects.filter(client_id=client_id)
    
# Essa classe é responsável por responder as requisições das urls:
# trail/<trail_pk>/steps e trail/<trail_pk>/steps/<step_pk> 
# Desta forma, ela implementa para cada um dos endpoints respectivamente GET e POST, PATCH e DELETE 
# Por fim, vale salientar que essa classe cria, deleta e atualiza os steps relacionados com 1 trail
@extend_schema(tags=['Etapas (aninhado)'])
class StepWithTrailViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return StepListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return StepWithTrailCreateSerializer
        return StepDetailSerializer
    
    def get_serializer_context(self):
        return {'trail_id': self.kwargs['trail_pk']}

# Essa classe é responsável por responder a requisições das urls:
# all-steps/ e all-steps/<step_pk>
# Nela você consegue manusear os steps diretamente, sem ter que passar pela trail/
@extend_schema(tags=['Etapas (global)'])
class OnlyStepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return StepListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return StepCreateSerializer
        return StepDetailSerializer

@extend_schema(tags=['Links (aninhado)'])
class LinksWithStepViewSet(viewsets.ModelViewSet):

    queryset = Links.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LinkWithStepCreateSerializer
        else:
            return LinkListSerializer
    
    def get_serializer_context(self):
        return {'step_id': self.kwargs['step_pk']}
    
@extend_schema(tags=['Links (Globais)'])
class OnlyLinksViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LinkCreateSerializer
        else:
            return LinkListSerializer

@extend_schema(tags=['Attachments (aninhado)'])
class AttachmentsViewSet(viewsets.ModelViewSet):
    queryset = Attachments.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AttachmentWithStepCreateSerializer
        else:
            return AttachmentListSerializer

    def get_serializer_context(self):   
        return {'step_id': self.kwargs['step_pk']}