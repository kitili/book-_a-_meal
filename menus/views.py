from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import menus
from .serializer import menusSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from users.models import Account
from users.api.serializers import ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
 
class menuslist(APIView):
     
     def get(self,request):
         menus1= menus.objects.all ()
         serializer=menusSerializer(menus1,many=True)
         return Response(serializer .data)
     

@api_view(['POST'])
def registeradmin(request):
    if request.method == 'POST':
        serializer = createSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save() 
            data = ProfileSerializer(account).data
        else:
            data = serializer.errors
        return Response(data=data)