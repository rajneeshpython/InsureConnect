from django.db import models

class Insurer(models.Model):
    name = models.CharField(max_length=255)
    api_url = models.URLField(help_text="External API endpoint for quotes/policy purchase")
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class InsurancePlan(models.Model):
    PLAN_TYPES = [
        ("motor", "Motor"),
        ("health", "Health"),
        ("life", "Life"),
    ]

    insurer = models.ForeignKey(Insurer, on_delete=models.CASCADE, related_name="plans")
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPES)
    plan_name = models.CharField(max_length=255)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)
    premium_base = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plan_name} ({self.plan_type})"
