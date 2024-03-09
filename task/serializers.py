from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


