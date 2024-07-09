from django.urls import path
from .apps import TasksConfig
from .views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, TaskDestroyAPIView

app_name = TasksConfig.name

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='create'),
    path('list/', TaskListAPIView.as_view(), name='list'),
    path('view/<int:pk>/', TaskRetrieveAPIView.as_view(), name='view'),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='delete'),
]
