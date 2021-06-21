from django.urls import include
from .views import BugViewSet
from rest_framework import routers


router = routers.SimpleRouter()

router.register('bug', BugViewSet)


urlpatterns = router.urls
