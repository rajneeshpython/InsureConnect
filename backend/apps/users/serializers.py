from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile, Role

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("role", "phone_number")


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='profile.role', read_only=True)
    phone_number = serializers.CharField(source='profile.phone_number', read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "role", "phone_number")


class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Role.choices, default=Role.CUSTOMER)
    phone_number = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "role", "phone_number")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        role = validated_data.pop("role", Role.CUSTOMER)
        phone_number = validated_data.pop("phone_number", "")
        password = validated_data.pop("password")

        # Create user
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        # Create associated profile
        UserProfile.objects.create(user=user, role=role, phone_number=phone_number)
        return user
