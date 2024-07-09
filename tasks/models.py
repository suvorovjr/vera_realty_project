import uuid
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    due_date = models.DateTimeField(blank=True, null=True, verbose_name='Срок выполнения')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress', verbose_name='Статус')

    def __str__(self):
        return f'Задача {self.title}, создана {self.created_at}.'

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(verbose_name='Тело комментария')
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE, verbose_name='Задача')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.task} - {self.text[:25]}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
