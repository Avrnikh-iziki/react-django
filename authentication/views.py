from django.shortcuts import render
from rest_framework import  generics, status
from rest_framework.response import Response
from . import serializer


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class Auth(generics.GenericAPIView):
    serializer_class = serializer.UserSerializer

    def post(self, request):
        data = request.data
        serializer=self.serializer_class(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser
        token["id"] = user.id
        token['username'] = user.username
        token['email'] = user.email
        token['phone_number'] =str(user.phone_number) 
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

