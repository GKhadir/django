from rest_framework import serializers
from .models import user

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields= '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['email','password']