from django.test import TestCase
from django.urls import reverse
from products.models import Product

class BagViewTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00,
            description='A test product',
            sku='TESTSKU'
        )

    def test_view_bag_get(self):
        """Test that the bag page loads successfully."""
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        """Test adding a product to the bag."""
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {'quantity': 2, 'redirect_url': reverse('view_bag')}
        )
        self.assertRedirects(response, reverse('view_bag'))
        session = self.client.session
        self.assertIn(str(self.product.id), session['bag'])
        self.assertEqual(session['bag'][str(self.product.id)], 2)

    def test_adjust_bag(self):
        """Test adjusting the quantity of a product in the bag."""
        # First, add to bag
        self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {'quantity': 2, 'redirect_url': reverse('view_bag')}
        )
        # Now adjust
        response = self.client.post(
            reverse('adjust_bag', args=[self.product.id]),
            {'quantity': 5, 'redirect_url': reverse('view_bag')}
        )
        self.assertRedirects(response, reverse('view_bag'))
        session = self.client.session
        self.assertEqual(session['bag'][str(self.product.id)], 5)

    def test_remove_from_bag(self):
        """Test removing a product from the bag."""
        # First, add to bag
        self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {'quantity': 2, 'redirect_url': reverse('view_bag')}
        )
        # Now remove
        response = self.client.post(
            reverse('remove_from_bag', args=[self.product.id])
        )
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        self.assertNotIn(str(self.product.id), session['bag'])