from django.test import TestCase
from django.urls import reverse


class ContactViewTest(TestCase):
    def test_contact_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
