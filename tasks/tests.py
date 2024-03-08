from django.test import TestCase
from tasks.models import Task

class TaskModelTestCase(TestCase):
    def test_task_creation(self):
        # Crea una instancia de Task
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task."
        )

        # Verifica que la instancia se haya creado correctamente
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task.")
        self.assertFalse(task.completed)  # Verifica que la tarea no esté marcada como completada por defecto

    def test_task_str_representation(self):
        # Crea una instancia de Task
        task = Task.objects.create(
            title="Another Test Task",
            description="Another test task."
        )

        # Verifica la representación de cadena del modelo
        self.assertEqual(str(task), "Another Test Task")