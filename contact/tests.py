from django.test import TestCase
from django.urls import reverse
from .models import Contact


class ContactViewTest(TestCase):
    def test_contact_get(self):
        """Test that the contact page loads successfully."""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_post(self):
        """Test submitting the contact form saves data and shows success."""
        data = {
            'name': 'Test User',
            'email': 'test@example.com'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Contact.objects.filter(
                name='Test User',
                email='test@example.com'
            ).exists()
        )
        self.assertContains(response, 'success')
