"""
This file contains the views for the tasks app.
"""

from rest_framework import generics
from .models import Task
from .serializer import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    """
    Vista para listar y crear tareas.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver, actualizar y eliminar tareas.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
