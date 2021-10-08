from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.registerUser),

    path('profiles/', views.userProfiles),
    path('profile/<str:pk>/', views.userProfile),
    path('profile/<str:pk>/edit/', views.updateProfile),
]