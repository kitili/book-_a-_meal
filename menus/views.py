from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import menus
from .serializer import menusSerializer
 
class menuslist(APIView):
     
     def get(self,request):
         menus1= menus.objects.all ()
         serializer=menusSerializer(menus1,many=True)
         return Response(serializer .data)
     
         
         