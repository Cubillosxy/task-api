from rest_framework import serializers
from api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'description',
            'done',
        )
        model = Task
