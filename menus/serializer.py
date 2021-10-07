from django.db.models import fields
from rest_framework import serializers
from. models import menus

class menusSerializer(serializers.ModelSerializer):
    class Meta:
        model = menus
        
        fields = '__all__'
        