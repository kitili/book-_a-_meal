from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('add/', views.addMenuItem),
    path('items/', views.getMenuItems),
    path('item/<str:pk>/', views.getSingleMenuItem),
    path('item/<str:pk>/edit/', views.updateMenuItem),
    path('item/<str:pk>/delete/', views.deleteMenuItem),
    path('item/<str:pk>/set/', views.setMenuItem),
]