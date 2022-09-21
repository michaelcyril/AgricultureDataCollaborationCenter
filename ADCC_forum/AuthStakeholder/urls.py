from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'AuthStakeholder'
urlpatterns = [
    path('register/user', RegisterUser),
    path('register/profile', CreateProfile),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]
