from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import UserProfile, Role

User = get_user_model()


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "phone_number", "created_at", "updated_at")
    list_filter = ("role", "created_at")
    search_fields = ("user__username", "user__email", "phone_number")
    ordering = ("-created_at",)


# Optional: make User inline with Profile for convenience
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profile"


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]


# Unregister default User and register with profile inline
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
