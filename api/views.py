from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


from api.models import Task

from rest_framework import generics
from rest_framework.authtoken.models import Token

from api.serializers import TaskSerializer


class BaseView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def base_perform(self, serializer):
        if not hasattr(self.request, 'user'):
            raise ValidationError('Invalid user')

        user = self.request.user
        serializer.save(user=user)


class TaskList(BaseView, generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = super().get_queryset()
        description = self.request.query_params.get('description', None)
        if description is not None:
            queryset = queryset.filter(description__icontains=description)

        return queryset

    def perform_create(self, serializer):
        self.base_perform(serializer)


class TaskDetail(BaseView, generics.RetrieveUpdateDestroyAPIView):
    def perform_update(self, serializer):
        self.base_perform(serializer)
