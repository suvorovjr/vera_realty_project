from rest_framework import generics, status
from rest_framework.response import Response
from .paginators import TaskPaginator
from .serializers import TaskSerializer, CommentSerializer
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


class TaskAsCompletedAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = 'completed'
        task.save()
        return Response({'status': 'task marked as completed'}, status=status.HTTP_200_OK)


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
