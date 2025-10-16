from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password']