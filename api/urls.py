from django.urls import path
from .views import RegisterView,alluser,LoginView,RefreshTokenView,AdminView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns =[
    path('userregister/',RegisterView.as_view(),name='userregister'),
    path('alluser/',alluser.as_view(),name='alluser'),
    path('login/',LoginView.as_view(),name='login'),
    path('adminregister/',AdminView.as_view(),name='adminregister'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
]
