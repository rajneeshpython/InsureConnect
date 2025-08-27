from rest_framework import serializers
from .models import Insurer, InsurancePlan

class InsurancePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePlan
        fields = ("id", "plan_type", "plan_name", "coverage_amount", "premium_base")


class InsurerSerializer(serializers.ModelSerializer):
    plans = InsurancePlanSerializer(many=True, read_only=True)

    class Meta:
        model = Insurer
        fields = ("id", "name", "api_url", "contact_email", "plans")
