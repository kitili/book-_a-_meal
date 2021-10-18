from django.contrib import auth

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import AuthenticationFailed

from users.models import Account

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email','username','date_joined','user_image','first_name','other_name']

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only':True},
            'email': {'validators':[]},
            'username': {'validators':[]}
        }

    def save(self):
        if Account.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'status':'fail', 'error': 'An account with this username exists'})
        
        if Account.objects.filter(email=self.validated_data['email']).exists():
           
            raise serializers.ValidationError({'status':'fail', 'error': 'An account with this email exists'})
        

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'status':'fail', 'error': 'Passwords must match!'})

        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )

        account.set_password(password)
        account.save()

        return account

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.CharField(max_length=255, min_length=6, read_only=True)
    tokens = serializers.DictField(tokens)
    class Meta:
        model = Account
        fields = ['id','email','username','date_joined','user_image','first_name','other_name','tokens', 'password','is_staff']

    def validate(self, data):
        email=data['email']
        password=data['password']
        
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed({'status':'fail', 'error': 'Invalid credentials!'})
        user.tokens = user.tokens()
        return user

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    class Meta:
        fields = ['email']

