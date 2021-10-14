# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import serializers, status
from menus.models import menus
from .serializers import menusSerializer
# from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from rest_framework.decorators import permission_classes
# from users.models import Account
# from users.api.serializers import ProfileSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from menus.models import menus
from menus.api.serializers import menusSerializer


 
class menuslist(APIView):
     
     def get(self,request):
         menus1= menus.objects.all ()
         serializer=menusSerializer(menus1,many=True)
         return Response(serializer .data)
     
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def addMenuItem(request):
    if request.method == 'POST':
        serializer = menusSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            menu_item = serializer.save(owner=request.user)
            data = menusSerializer(menu_item).data
        else:
            data = serializer.errors
        return Response(data=data)     
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMenuItems(request):
    try:
        menus1 = menus.objects.all()
    except menus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = menusSerializer(menus1, many=True)
        data = serializer.data
        return Response({'status':'success','data':data}, status=status.HTTP_200_OK)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSingleMenuItem(request,pk):
    try:
        menu = menus.objects.get(id=pk)
    except menus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = menusSerializer(menu)
        return Response(serializer.data)
        
        
        
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def updateMenuItem(request,pk):
    try:
        menu = menus.objects.get(id=pk)
    except menus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = menusSerializer(menu, data=request.data)
        if serializer.is_valid():
            menu_item = serializer.save()
            return Response(menusSerializer(menu_item).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
     
     
     
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def deleteMenuItem(request,pk):
	try:
		menu_item = menus.objects.get(id=pk)
	except menus.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'DELETE':
		operation = menu_item.delete()
		data = {}
		if operation:
			data['response'] = 'Menu item has been deleted.'
		return Response(data=data)