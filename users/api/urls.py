from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('login/', views.loginUser),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.registerUser),

    path('profiles/', views.userProfiles),
    path('profile/<str:pk>/', views.userProfile),
    path('profile/<str:pk>/edit/', views.updateProfile),

    path('change-password-request/', views.requestPasswordReset, name='change-password-request'),
    path('change-password/<str:uidb64>/<str:token>/', views.resetPassword, name='change-password-reset'),
]