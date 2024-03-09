"""
Este módulo contiene las pruebas unitarias para el modelo Task.
"""

from django.test import TestCase
from tasks.models import Task


class TaskModelTestCase(TestCase):
    """
    Clase de pruebas para el modelo Task.
    """
    
    def test_task_creation(self):
        """
        Prueba la creación de una tarea.
        """
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task."
        )

        # Verifica que la instancia se haya creado correctamente
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task.")
        self.assertFalse(task.completed)  

    def test_task_str_representation(self):
        """
        Prueba la representación de cadena de una tarea.
        """
        task = Task.objects.create(
            title="Another Test Task",
            description="Another test task."
        )

        # Verifica la representación de cadena del modelo
        self.assertEqual(str(task), "Another Test Task")
