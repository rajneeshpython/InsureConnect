# apps/users/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import UserProfile, Role

User = get_user_model()


class UsersAPITest(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.me_url = reverse('current_user')
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "TestPass123!",
            "role": Role.CUSTOMER,
            "phone_number": "9998887776"
        }

    def create_user_with_profile(self, data=None):
        """Helper to create user + profile"""
        data = data or self.user_data
        user = User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"]
        )
        UserProfile.objects.create(
            user=user,
            role=data.get("role", Role.CUSTOMER),
            phone_number=data.get("phone_number", "")
        )
        return user

    def test_user_registration(self):
        """Test that a new user can register and profile is created"""
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username=self.user_data["username"])
        self.assertTrue(UserProfile.objects.filter(user=user).exists())
        self.assertEqual(user.profile.role, Role.CUSTOMER)

    def test_user_login(self):
        """Test that a registered user can log in and get JWT tokens"""
        self.create_user_with_profile()
        response = self.client.post(self.login_url, {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_get_current_user(self):
        """Test retrieving current logged-in user's profile"""
        user = self.create_user_with_profile()
        # Log in to get JWT token
        login_response = self.client.post(self.login_url, {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }, format='json')
        access_token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Retrieve current user
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['role'], user.profile.role)
        self.assertEqual(response.data['phone_number'], user.profile.phone_number)
