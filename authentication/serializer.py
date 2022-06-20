from .models import User
from rest_framework.validators import  ValidationError
from rest_framework import serializers,status
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model= User
        fields=['id','username','email','phone_number','password']
        extra_kwargs ={"password":{"write_only":True}}


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self,attrs):
        email=User.objects.filter(email=attrs.get('email')).exists()
        username=User.objects.filter(username=attrs.get('username')).exists()
        phone_number=User.objects.filter(phone_number=attrs.get('phone_number')).exists()

        if email: raise ValidationError(detail="User with email exists",code=status.HTTP_403_FORBIDDEN)
        if username: raise ValidationError(detail="User with username exists",code=status.HTTP_403_FORBIDDEN)
        if phone_number: raise ValidationError(detail="User with phone number exists",code=status.HTTP_403_FORBIDDEN)            

        return super().validate(attrs) 

 

