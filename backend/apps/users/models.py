from django.conf import settings
from django.db import models


class Role(models.TextChoices):
    CUSTOMER = "customer", "Customer"
    AGENT = "agent", "Agent"
    ADMIN = "admin", "Admin"


class UserProfile(models.Model):
    """
    InsureConnect profile attached to Django's built-in User.
    Keeps marketplace-specific fields without replacing the auth model.
    Safe choice since you already created a superuser.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
        help_text="Access level for workflows (customer/agent/admin)."
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        help_text="Customer/Agent contact number used in quotes & notifications."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    @property
    def is_customer(self):
        return self.role == Role.CUSTOMER

    @property
    def is_agent(self):
        return self.role == Role.AGENT

    @property
    def is_admin(self):
        return self.role == Role.ADMIN
