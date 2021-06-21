
# Create your views here.
from .models import Bug
from .serializers import BugSerializer
from rest_framework import permissions
from dynamic_rest import viewsets
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_api_key.permissions import HasAPIKey


class BugViewSet(viewsets.DynamicModelViewSet):

    permission_classes = [permissions.IsAdminUser | HasAPIKey]

    throttle_classes = [UserRateThrottle]

    queryset = Bug.objects.all()

    serializer_class = BugSerializer
