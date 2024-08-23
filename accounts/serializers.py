from rest_framework import serializers
# from django.contrib.auth.models import User
from accounts.models import User
from django.contrib.auth import authenticate
from django.utils.encoding import force_bytes,smart_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    token = serializers.CharField(max_length=555,read_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password','password2', 'tc','token' ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    token = serializers.CharField(max_length=555,read_only=True)
    class Meta:
        model = User
        fields = ['email',  'password','token'  ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        # doing validation in views
    # def validate(self, attrs):
    #     email = attrs.get('email')
    #     password = attrs.get('password')
    #     user = authenticate(email=email,password=password)
    #     if user is not None:
    #         return attrs
    #     else:
    #         raise serializers.ValidationError("Email or Password is not Valid")
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']
        
class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255,style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['password','password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        
        return attrs
    
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']
        
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id)) 
            print(uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print(token)
            link = 'http://localhost:8000/api/user/reset-password/'+uid+'/'+token
            print(link)
            # send email 
            body = 'Click on the link to reset your password '+link
            data = {
                'subject':'Reset Your Password',
                'body':body,
                'to_email':user.email
            }
            Util.send_email(data)               
            
            return attrs  
        else:
            raise serializers.ValidationError("You are not a Registered User")  
        
class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255,style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['password','password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError("Token is not Valid or Expired")
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError("Token is not Valid or Expired")