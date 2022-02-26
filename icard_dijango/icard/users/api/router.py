from django.urls import path
from posixpath import basename
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,)
from users.api.views import UserApiViewSet, UserView

router_user = DefaultRouter()

router_user.register(
    prefix='user', basename='users', viewset=UserApiViewSet
)

urlPatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserView.as_view())
]