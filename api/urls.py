from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns =[
    path('userregister/',userRegisterView.as_view(),name='userregister'),
    path('alluser/',alluser.as_view(),name='alluser'),
    path('login/',LoginView.as_view(),name='login'),
    path('adminregister/',adminRegisterView.as_view(),name='adminregister'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('profile/', profileView.as_view(), name='profile'),
    path('edituser/<str:email>/', allCrudView.as_view(), name='edituser')    
    ]
