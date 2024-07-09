from rest_framework import serializers
from .models import Task, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer()

    class Meta:
        model = Task
        fields = '__all__'
