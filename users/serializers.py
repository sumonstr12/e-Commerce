from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ["username", "email", "mobile", "password"]

    def create(self, validated_data):
        # password = validated_data.pop("password")
        # user = User(**validated_data)
        # user.set_password(password)
        # user.save()
        # return user
    
        # alter way
        user = User(
            username = validated_data["username"],
            email = validated_data["email"],
            mobile = validated_data["mobile"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
    

class UserProfileSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "mobile",
        ]