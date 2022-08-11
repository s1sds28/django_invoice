# from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

# Create your tests here.
class InvoiceTests(APITestCase):
    fixtures = ["main.json"]

    # Create test, ensure we can create a new invoice object
    def test_create_invoice(self):
        self.client.login(username='admin', password='testpass123')
        url = reverse('invoice-list')
        data = {
        "title": "test",
        "owner": 1,
        "bill_to": "test",
        "bill_from": "test",
        "line_item": "test",
        "monetary_value": 1
        }
        response = self.client.post(url, data, format='json')
        self.client.logout()
        self.assertEqual(response.status_code, 201)

    # Read test, ensure we can read a invoice
    def test_read_invoice(self):
        self.client.login(username='admin', password='testpass123')
        url = reverse('invoice-detail', args='1')
        response = self.client.get(url, format='json')
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    # Update test, ensure we can unpdate an invoice
    def test_update_invoice(self):
        self.client.login(username='admin', password='testpass123')
        url = reverse('invoice-detail', args='1')
        data = {
        "monetary_value": 123456789
        }
        response = self.client.put(url, data, format='json')
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Delete test, ensure we can delete an invoice
    def test_delete_invoice(self):
        self.client.login(username='admin', password='testpass123')
        url = reverse('invoice-detail', args='1')
        response = self.client.delete(url)
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
