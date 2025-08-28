from django.contrib import admin
from .models import QuoteRequest, Quote


class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 1


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "insurance_type", "created_at")
    search_fields = ("user__username", "user__email")
    list_filter = ("insurance_type", "created_at")
    ordering = ("-created_at",)
    inlines = [QuoteInline]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "quote_request", "insurer", "plan", "premium", "coverage_amount", "created_at")
    search_fields = ("insurer__name", "plan__plan_name", "quote_request__user__username")
    list_filter = ("insurer", "plan", "created_at")
    ordering = ("-created_at",)
