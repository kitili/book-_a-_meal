from django.db import models

class menus(models.Model):
    foodname=models.CharField(max_length=40)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=20)
    
    def _str_(self):
        return self.foodname
