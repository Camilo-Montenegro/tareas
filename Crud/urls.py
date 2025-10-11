from rest_framework import routers
from .api import TaskViewSet        

router=  routers.DefaultRouter()

router.register('api/Task', TaskViewSet, 'Task')
urlpatterns = router.urls
