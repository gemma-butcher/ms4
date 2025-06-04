from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import FAQCategory, FAQ


class FAQViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.admin = User.objects.create_superuser(
            'admin', 'admin@test.com', 'password'
        )
        self.client.login(username='admin', password='password')
        self.category = FAQCategory.objects.create(name="General")
        self.faq = FAQ.objects.create(
            category=self.category,
            question="What is this?",
            answer="A test FAQ."
        )

    def test_faq_list_view(self):
        url = reverse('faq_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "What is this?")

    def test_faq_create_view(self):
        url = reverse('faq_create')
        data = {
            'category': self.category.id,
            'question': 'New FAQ?',
            'answer': 'Yes, it works!'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(FAQ.objects.filter(question='New FAQ?').exists())

    def test_faq_update_view(self):
        url = reverse('faq_update', args=[self.faq.id])
        data = {
            'category': self.category.id,
            'question': 'Updated?',
            'answer': 'Updated answer.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.faq.refresh_from_db()
        self.assertEqual(self.faq.question, 'Updated?')

    def test_faq_delete_view(self):
        url = reverse('faq_delete', args=[self.faq.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(FAQ.objects.filter(id=self.faq.id).exists())