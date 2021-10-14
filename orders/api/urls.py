from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.createOrder),
    path('fetch-order/<str:pk>/', views.fetchOrder),
    path('fetch-orders/', views.fetchOrders),
    path('fetch-summary/', views.fetchSummary),
    path('fetch-order-history/', views.fetchOrderHistory),
    path('delete-order/<str:pk>/', views.deleteOrder),
    path('delete-order-item/<str:order_id>/<str:item_id>/', views.deleteOrderItem),
    path('edit-order/<str:order_id>/<str:item_id>/', views.updateOrder),
    path('close-order/<str:pk>/', views.closeOrder),
]