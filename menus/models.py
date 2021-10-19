from django.db import models
import uuid
from users.models import Account
from cloudinary.models import CloudinaryField

class menus(models.Model):
    owner = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    menu_image = models.ImageField(upload_to='images/menus/')
    created = models.DateTimeField(auto_now_add=True)
    days_selection = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    