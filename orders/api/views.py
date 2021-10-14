import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from orders.api.serializers import OrderItemSerializer, OrderSerializer, AddOrderSerializer
from users.api.serializers import ProfileSerializer
from orders.models import Order, OrderItem
from menus.models import menus

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createOrder(request):
    serializer = AddOrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = request.user
    menuObj = menus.objects.get(id=request.data['menu_id'])
    
    try:
        orderObj = user.order_set.get(is_open=True)
    except Order.DoesNotExist:
        orderObj = Order()
        orderObj.customer = user
        orderObj.save()

    if request.method == 'POST':
        try:
            quantity = int(request.data['quantity'])
            orderItemObj = OrderItem(
                order=orderObj, 
                menu_item=menuObj, 
                quantity=quantity, 
                price=menuObj.price,
                total=quantity * menuObj.price
            )

            orderItemObj.save()

            orderObj.getOrderTotal

            searializer = OrderSerializer(orderObj)
            return Response(searializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error':'This menu item is in your cart.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetchOrder(request,pk):
    try:
        orderObj = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return Response({'error':'The order does not exist!'},status=status.HTTP_404_NOT_FOUND)
    
    searializer = OrderSerializer(orderObj)
    return Response(searializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def fetchOrders(request):
    try:
        orderObj = Order.objects.all()
    except Order.DoesNotExist:
        return Response({'error':'There are no orders!'},status=status.HTTP_404_NOT_FOUND)
    
    searializer = OrderSerializer(orderObj, many=True)
    return Response(searializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteOrder(request,pk):
    try:
        order = Order.objects.get(id=pk)
        if not order.is_open:
            return Response({'status':'fail', 'error': 'Cannot delete a closed order.'}, status=status.HTTP_404_NOT_FOUND)
    except Order.DoesNotExist:
        return Response({'error':'The order does not exist.'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        order.delete()
        return Response({'response':'The order has been deleted.'}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteOrderItem(request,order_id,item_id):
    try:
        order = Order.objects.get(id=order_id)
        if not order.is_open:
            return Response({'status':'fail', 'error': 'Cannot delete a closed order.'}, status=status.HTTP_404_NOT_FOUND)
    except Order.DoesNotExist:
        return Response({'status':'fail','error':'The order does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    order_items = OrderItem.objects.filter(order=order)
    if order_items.exists():
        if order_items.count() > 1:
            order_item = OrderItem.objects.get(id=item_id)
            order_item.delete()
            order.getOrderTotal
            return Response({'status':'success', 'response':'The order item has been deleted.'}, status=status.HTTP_200_OK)
        else:
            order.delete()
            return Response({'status':'success', 'response':'The order has been deleted.'}, status=status.HTTP_200_OK)     
    else:
        return Response({'status':'fail','error':'The order item does not exist.'},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrder(request, order_id, item_id):
    serializer = AddOrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        order = Order.objects.get(id=order_id)
        if not order.is_open:
            return Response({'status':'fail', 'error': 'Cannot edit a closed order.'}, status=status.HTTP_404_NOT_FOUND)
    except Order.DoesNotExist:
        return Response({'status':'fail', 'error': 'The order does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    order_item = OrderItem.objects.get(id=item_id, order=order)
    if order_item:
        quantity = int(request.data['quantity'])
        order_item.quantity = quantity
        order_item.total = quantity * order_item.price

        order_item.save()

        order.getOrderTotal

        data = OrderSerializer(order).data
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({'status':'fail','error':'The order item does not exist.'},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def closeOrder(request,pk):
    try:
        order = Order.objects.get(id=pk)
        if order.is_open:
            order.is_open=False
            order.save()
            data = OrderSerializer(order).data
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'status':'fail','error':'The order is already closed.'},status=status.HTTP_404_NOT_FOUND)
    except Order.DoesNotExist:
        return Response({'status':'fail', 'error': 'The order does not exist.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetchOrderHistory(request):
    try:
        orders = Order.objects.filter(customer=request.user)
        searializer = OrderSerializer(orders, many=True)
        return Response(searializer.data, status=status.HTTP_200_OK)
    except Order.DoesNotExist:
        return Response({'status':'fail', 'error': 'You do not have an order history.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def fetchSummary(request):
    # try:
    current_date = datetime.date.today()
    orders_today = Order.objects.filter(created__date=current_date, is_open=False)
    if orders_today.count() >= 1:
        amount = 0
        for order in orders_today:
            amount +=order.total_amount
        
        serializer =OrderSerializer(orders_today, many=True)
        data = {
            'numberOfTransactions': orders_today.count(),
            'amount': amount,
            'transactions': serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)
    return Response({'error':'There were no orders made today!'},status=status.HTTP_404_NOT_FOUND)
    