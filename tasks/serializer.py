"""
The serializers in Django REST framework work very similarly to Django's Form and ModelForm classes.
"""

from rest_framework import serializers
from .models import Task

"""
Serializador para el modelo Task.
"""

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description']
