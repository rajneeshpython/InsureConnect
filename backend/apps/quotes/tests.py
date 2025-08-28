# apps/quotes/tests.py
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..insurers.models import Insurer, InsurancePlan
from .models import QuoteRequest, Quote

User = get_user_model()


class QuoteRequestTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="customer", password="password123"
        )
        self.client.force_authenticate(user=self.user)

        # Sample insurer + plan
        self.insurer = Insurer.objects.create(name="Test Insurer")
        self.plan = InsurancePlan.objects.create(
            insurer=self.insurer,
            plan_name="Basic Health Plan",
            coverage_amount=100000,
            premium_base=5000
        )

    def create_quote_request(self):
        """Helper to create a QuoteRequest for this user"""
        return QuoteRequest.objects.create(
            user=self.user,
            insurance_type="health",
            details={"age": 30, "city": "Delhi"}
        )

    def create_quote(self, qr):
        """Helper to create a Quote linked to a QuoteRequest"""
        return Quote.objects.create(
            quote_request=qr,
            insurer=self.insurer,
            plan=self.plan,
            premium=5000,
            coverage_amount=100000,
            response_data={"note": "Test offer"}
        )

    def test_create_quote_request(self):
        url = reverse("quote-request-list")  # from DRF router
        payload = {"insurance_type": "health", "details": {"age": 28, "city": "Mumbai"}}

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(QuoteRequest.objects.count(), 1)
        self.assertEqual(QuoteRequest.objects.first().insurance_type, "health")

    def test_list_quote_requests(self):
        qr = self.create_quote_request()
        url = reverse("quote-request-list")

        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["insurance_type"], qr.insurance_type)

    def test_list_quotes_for_request(self):
        qr = self.create_quote_request()
        self.create_quote(qr)

        url = reverse("quote-list")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(str(response.data[0]["premium_amount"]), "5000.00")
