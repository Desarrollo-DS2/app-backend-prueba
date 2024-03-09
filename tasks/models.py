"""
Este módulo contiene la definición de los modelos de la aplicación de tareas.
"""

from django.db import models

""" 
Modelo de tarea.
"""

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
