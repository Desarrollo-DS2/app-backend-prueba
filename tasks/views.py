"""
This file contains the views for the tasks app.
"""

from rest_framework import generics
from .models import Task
from .serializer import TaskSerializer

"""
Vista para listar y crear tareas.
"""

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

"""
Vista para ver, actualizar y eliminar tareas.
"""

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
