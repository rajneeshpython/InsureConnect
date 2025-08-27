from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Insurer, InsurancePlan
from ..users.models import UserProfile, Role

User = get_user_model()


class InsurersAPITest(APITestCase):

    def setUp(self):
        # Create a user and profile for authentication
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="TestPass123!"
        )
        UserProfile.objects.create(user=self.user, role=Role.ADMIN)

        # Log in and get JWT token
        self.login_url = reverse("token_obtain_pair")
        response = self.client.post(self.login_url, {
            "username": "testuser",
            "password": "TestPass123!"
        }, format='json')
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # URLs
        self.insurer_list_url = reverse("insurer_list")
        self.plan_list_url = reverse("plan_list")

        # Mock Insurers and Plans
        self.insurer1 = Insurer.objects.create(
            name="HDFC Life",
            api_url="https://api.hdfclife.com",
            contact_email="contact@hdfclife.com"
        )
        self.insurer2 = Insurer.objects.create(
            name="ICICI Lombard",
            api_url="https://api.icicilombard.com",
            contact_email="contact@icicilombard.com"
        )

        self.plan1 = InsurancePlan.objects.create(
            insurer=self.insurer1,
            plan_type="life",
            plan_name="HDFC Life Secure",
            coverage_amount=1000000,
            premium_base=10000
        )

        self.plan2 = InsurancePlan.objects.create(
            insurer=self.insurer2,
            plan_type="health",
            plan_name="ICICI Health Protect",
            coverage_amount=500000,
            premium_base=5000
        )

    def test_get_all_insurers(self):
        """Test retrieving all insurers with their plans"""
        response = self.client.get(self.insurer_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn("HDFC Life", [i['name'] for i in response.data])

    def test_get_all_plans(self):
        """Test retrieving all insurance plans"""
        response = self.client.get(self.plan_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn("HDFC Life Secure", [p['plan_name'] for p in response.data])
