from django.db import models
import uuid

from users.models import Account
from menus.models import menus
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True, null=True)
    total_amount = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    @property
    def getOrderTotal(self):    
        order_items = self.orderitem_set.all()
        amount = 0
        for order in order_items:
           amount +=order.total
        
        self.total_amount = amount
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(menus, null=True, blank=True, on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    price = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    class Meta:
        unique_together = [['order', 'menu_item']]