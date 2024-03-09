"""
Este módulo contiene la definición de los modelos de la aplicación de tareas.
"""

from django.db import models

class Task(models.Model):
    """
    Modelo de tarea.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """
        Devuelve una representación de cadena de la tarea.
        """
        return self.title
