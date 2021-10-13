# from django.db import models

# class menus(models.Model):
#     foodname=models.CharField(max_length=40)
#     description=models.TextField()
#     price=models.DecimalField(decimal_places=2, max_digits=20)
    
#     def _str_(self):
#         return self.foodname

from django.db import models
import uuid
from users.models import Account


class menus(models.Model):
    owner = models.ForeignKey(
        Account, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    menu_image = models.ImageField(upload_to='menus/')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.name