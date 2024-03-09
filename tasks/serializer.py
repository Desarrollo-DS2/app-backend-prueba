"""
The serializers in Django REST framework work very similarly to Django's Form and ModelForm classes.
"""

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Task.
    """
    class Meta:
        model = Task
        fields = ['id', 'title', 'description']
