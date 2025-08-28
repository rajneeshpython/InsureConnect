from rest_framework import serializers
from .models import Quote, QuoteRequest

class QuoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteRequest
        fields = ["id", "insurance_type", "details", "created_at"]


class QuoteSerializer(serializers.ModelSerializer):
    # Expose premium as "premium_amount" for compatibility
    premium_amount = serializers.DecimalField(
        source="premium", max_digits=12, decimal_places=2, read_only=True
    )

    class Meta:
        model = Quote
        fields = [
            "id",
            "quote_request",
            "insurer",
            "plan",
            "premium_amount",
            "coverage_amount",
            "response_data",
            "created_at",
        ]
