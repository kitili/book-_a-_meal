from rest_framework import serializers

from orders.models import OrderItem, Order
from users.api.serializers import ProfileSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.SlugRelatedField(
        slug_field='name',
        many=False,
        read_only=True
    )
    class Meta:
        model = OrderItem
        fields = ['id','order','menu_item','quantity','price','total']
    

class OrderSerializer(serializers.ModelSerializer):
    customer = ProfileSerializer(many=False)
    orders = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'

    def get_orders(self, obj):
        
        orders = obj.orderitem_set.all()
        serializer = OrderItemSerializer(orders, many=True)
        return serializer.data

class AddOrderSerializer(serializers.Serializer):
    menu_id = serializers.CharField(min_length=6, max_length=68, write_only=True)
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        fields = ['menu_id','quantity']
        extra_kwargs = {
            'menu_id': {'required': True},
            'quantity': {'required': True},
        } 