"""
Este módulo contiene la configuración para la interfaz de administración de Django.
"""

from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)
