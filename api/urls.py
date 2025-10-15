from django.urls import path
from .views import RegisterView,alluser,LoginView,RefreshTokenView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns =[
    path('register/',RegisterView.as_view(),name='register'),
    path('alluser/',alluser.as_view(),name='alluser'),
    path('login/',LoginView.as_view(),name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
]
