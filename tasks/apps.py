"""
Este módulo define la configuración de la aplicación de tareas.
"""

from django.apps import AppConfig

class TasksConfig(AppConfig):
    """
    Configuración de la aplicación de tareas.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
