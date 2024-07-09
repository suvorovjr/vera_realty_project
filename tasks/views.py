from rest_framework import generics
from .paginators import TaskPaginator
from .serializers import TaskSerializer
from .models import Task


class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    pagination_class = TaskPaginator


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
