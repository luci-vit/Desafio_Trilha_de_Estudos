from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('trails', views.TrailViewSet, basename='trails')
router.register('all-steps', views.OnlyStepViewSet, basename='all-steps')
router.register('all-links', views.OnlyLinksViewSet, basename='all-links')
router.register('clients', views.ClientsViewSet, basename='clients')


trails_routers = routers.NestedDefaultRouter(router, 'trails', lookup='trail')
trails_routers.register('steps', views.StepWithTrailViewSet, basename='trail-steps')

steps_routers = routers.NestedDefaultRouter(trails_routers, 'steps', lookup='step')
steps_routers.register('links', views.LinksWithStepViewSet, basename='step-links')
steps_routers.register('attachments', views.AttachmentsViewSet, basename='step-attachments')

all_steps_routers = routers.NestedDefaultRouter(router, 'all-steps', lookup='step')
all_steps_routers.register('links', views.OnlyLinksViewSet, basename='all-step-links')
all_steps_routers.register('attachments', views.AttachmentsViewSet, basename='all-step-attachments')


client_routers = routers.NestedDefaultRouter(router, 'clients', lookup='client')
client_routers.register('client-progress', views.ClientProgressWithClientViewSet, basename='client-progress')

urlpatterns = router.urls + trails_routers.urls + steps_routers.urls + all_steps_routers.urls + client_routers.urls