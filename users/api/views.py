from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from users.api.serializers import ProfileSerializer, RegistrationSerializer, ResetPasswordSerializer, LoginSerializer
from users.api.forms import ResetPasswordForm
from users.models import Account

@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        account = serializer.save() 
        data = ProfileSerializer(account).data
        
        return Response({'status': 'success', 'data': data})

@api_view(['POST'])
def loginUser(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.data

    return Response({'status':'success','data':data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def userProfiles(request):
    try:
        profiles = Account.objects.all()
    except Profile.DoesNotExist:
        return Response({'status':'fail','error':'There are no user profiles.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profiles, many=True)
        data = serializer.data
        return Response({'status':'success','data':data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userProfile(request,pk):
    try:
        profile = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        return Response({'status':'fail','error':'The user does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        data = serializer.data
        return Response({'status':'success','data':data}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request,pk):
    try:
        profile = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        return Response({'status':'fail','error':'User profile does not exist.'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response({'status':'success','data':data}, status=status.HTTP_201_CREATED)
            # return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def requestPasswordReset(request):
    serializer = ResetPasswordSerializer(data=request.data)
    if serializer.is_valid():
        try:
            email = request.data['email']
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return Response({'status':'fail','error':'Invalid email!'},status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'POST':
            serializer = ResetPasswordSerializer(data=request.data)
            if serializer.is_valid():
                uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
                token = PasswordResetTokenGenerator().make_token(user)
                current_site = get_current_site(request).domain
                relative_route = reverse('change-password-reset', kwargs={'uidb64':uidb64,'token':token})
                site_url = f'http://{current_site}{relative_route}'
                # Send email
                subject = 'Password Reset'
                message=f'Hi, \n use the link below to reset your password.\n{site_url}'

                send_mail(
                    subject, 
                    message, 
                    settings.EMAIL_HOST_USER, 
                    [email],
                    fail_silently=False
                )

                return Response({'status':'success','message':'Password reset email has been sent.'},status=status.HTTP_200_OK)
    else:
        return Response(data=serializer.errors)

def resetPassword(request,uidb64,token):
    try:
        pk = smart_str(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(id=pk)

        if not PasswordResetTokenGenerator().check_token(user, token):
            return render(request, 'reset_password_error.html', {'error':'Invalid token, kindly request a new one.'})
        
        if request.method == 'POST':
            form = ResetPasswordForm(data=request.POST)
            if form.is_valid():
                password = request.POST['password']
                password2 = request.POST['password2']

                if password != password2:
                    messages.error(request, 'Passwords must match')
                else:
                    user.set_password(password)
                    user.save()
                    return render(request, 'reset_password_complete.html')
            else:
                messages.error(request, 'Enter passwords')

        return render(request, 'reset.html')
    except DjangoUnicodeDecodeError as identifier:
        return render(request, 'reset_password_error.html', {'error':'Invalid token, kindly request a new one.'})

