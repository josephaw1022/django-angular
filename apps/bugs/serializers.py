from rest_framework import serializers
from .models import *
from dynamic_rest import serializers


class BugSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = Bug
        name = "Problem"
        fields = ['id', "title", "description",
                  "completed", "owner", "started"]
