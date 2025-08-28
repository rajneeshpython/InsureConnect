from django.db import models
from django.conf import settings
from ..insurers.models import Insurer, InsurancePlan

class QuoteRequest(models.Model):
    INSURANCE_TYPES = [
        ("motor", "Motor"),
        ("health", "Health"),
        ("life", "Life"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quote_requests"
    )
    insurance_type = models.CharField(max_length=20, choices=INSURANCE_TYPES)
    details = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QuoteRequest {self.id} by {self.user.username}"


class Quote(models.Model):
    quote_request = models.ForeignKey(
        QuoteRequest,
        on_delete=models.CASCADE,
        related_name="quotes"
    )
    insurer = models.ForeignKey(
        Insurer,
        on_delete=models.CASCADE,
        related_name="quotes",
        null=True,
        blank=True
    )
    plan = models.ForeignKey(
        InsurancePlan,
        on_delete=models.CASCADE,
        related_name="quotes",
        null=True,
        blank=True
    )
    premium = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    response_data = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote {self.id} for Request {self.quote_request.id}"
