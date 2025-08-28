from django.contrib import admin
from .models import Insurer, InsurancePlan


@admin.register(Insurer)
class InsurerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "api_url", "contact_email", "created_at")
    search_fields = ("name", "contact_email")
    ordering = ("-created_at",)


@admin.register(InsurancePlan)
class InsurancePlanAdmin(admin.ModelAdmin):
    list_display = ("id", "plan_name", "plan_type", "coverage_amount", "premium_base", "insurer", "created_at")
    list_filter = ("plan_type", "insurer")
    search_fields = ("plan_name", "insurer__name")
    ordering = ("-created_at",)
