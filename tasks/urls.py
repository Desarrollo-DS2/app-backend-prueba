"""
Este módulo define las URL de la aplicación de tareas.
"""

from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]
