from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo

class TodoViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.todo = Todo.objects.create(title="Test Todo", description="Test Description")

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")

    def test_detail_view(self):
        response = self.client.get(reverse('detail', args=[self.todo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Description")

    def test_add_view(self):
        response = self.client.post(reverse('add'), {
            'title': 'New Todo',
            'description': 'New Description',
            'completed': False,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(title='New Todo').exists())

    def test_edit_view(self):
        response = self.client.post(reverse('edit', args=[self.todo.id]), {
            'title': 'Updated Todo',
            'description': 'Updated Description',
            'completed': True,
        })
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Todo')

    def test_delete_view(self):
        response = self.client.post(reverse('delete', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())
