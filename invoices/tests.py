from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from invoices.models import Invoice

from django.contrib.auth.models import Group

import json

from .views import InvoiceDetail

from django.test.client import encode_multipart, RequestFactory



# Create your tests here.
class InvoiceTests(APITestCase):
    fixtures = ["main.json"]

    # Create test
    def test_create_invoice(self):
        self.client.login(username='admin', password='testpass123')
        """
        ensure we can create a new invoice object
        """
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
    # Read test
    def test_read_invoice(self):
        self.client.login(username='admin', password='testpass123')
        """
        ensure we can read a invoice
        """

        url = reverse('invoice-detail', args='1')
        response = self.client.get(url, format='json')
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    # Update
    def test_update_invoice(self):
        self.client.login(username='admin', password='testpass123')
        new_value = 123456789
        """
        ensure we can update an invoice
        """
        url = reverse('invoice-detail', args='1')
        data = {
        "monetary_value": new_value
        }

        response = self.client.put(url, data, format='json')
        # self.assertEqual(response.status_code, 200)
        query = self.client.get('/invoices/1/')
        query = json.loads(query.content)
        query = query.get('monetary_value')
        self.client.logout()
        self.assertEqual(query, new_value)

    # Delete
    def test_delete_invoice(self):
        self.client.login(username='admin', password='testpass123')
        """
        ensure we can delete an invoice
        """
        url = reverse('invoice-detail', args='1')
        response = self.client.delete(url)
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
