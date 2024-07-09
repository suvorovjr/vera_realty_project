from django.urls import path
from .apps import TasksConfig
from .views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, TaskDestroyAPIView, \
    TaskAsCompletedAPIView, CommentCreateAPIView

app_name = TasksConfig.name

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='create'),
    path('list/', TaskListAPIView.as_view(), name='list'),
    path('view/<uuid:pk>/', TaskRetrieveAPIView.as_view(), name='view'),
    path('update/<uuid:pk>/', TaskUpdateAPIView.as_view(), name='update'),
    path('delete/<uuid:pk>/', TaskDestroyAPIView.as_view(), name='delete'),
    path('change-status/<uuid:pk>/', TaskAsCompletedAPIView.as_view(), name='change-status'),
    path('add-comment/', CommentCreateAPIView.as_view(), name='add-comment'),
]
