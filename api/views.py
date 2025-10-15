from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import user
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from django.contrib.auth.hashers import make_password,check_password   
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def post(self,request):
        request.data['password']=make_password(request.data['password'])
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Registered Successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class alluser(APIView):
    def get(self,request):
        users=user.objects.all()
        serializer=RegisterSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request):
        try:
            log = user.objects.get(email=request.data['email'])
            if check_password(request.data['password'], log.password):
                serializer = RegisterSerializer(log)
                
                # Generate JWT tokens
                refresh = RefreshToken.for_user(log)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                return Response({
                    'user': serializer.data,
                    'access': access_token,
                    'refresh': refresh_token
                }, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)
        except user.DoesNotExist:
            return Response({"message": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            return Response({
                "access": access_token,
                "refresh": str(refresh)
            }, status=status.HTTP_200_OK)

        except TokenError as e:
            return Response({"error": "Invalid or expired refresh token"}, status=status.HTTP_401_UNAUTHORIZED)