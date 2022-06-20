import math
from django.shortcuts import render , get_object_or_404
from rest_framework import  generics, status
from rest_framework.response import Response
from .models import Products
from . import serializer
from rest_framework.permissions import IsAdminUser 


class AllProducts(generics.GenericAPIView):
    serializer_class = serializer.ProductsSerializer
    queryset = Products.objects.all()

    def get(self,request, number_pag=1):
        products = Products.objects.all().order_by("updated_at").reverse()[(number_pag -1 )*8: number_pag*8]
        pages= math.ceil(Products.objects.all().count() /8)
        serializer=self.serializer_class(instance=products, many=True)
        return Response(data= {'product': serializer.data ,'pages':pages }  ,status=status.HTTP_200_OK)

class AddProduct(generics.GenericAPIView):
    serializer_class = serializer.ProductsSerializer
    permission_classes = [IsAdminUser]
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductsManagment(generics.GenericAPIView):
    serializer_class = serializer.ProductsSerializer
    permission_classes = [IsAdminUser]

    def put(self , request , product_id):
        product=get_object_or_404(Products,pk=product_id)
        new_data_product = request.data
        serializer=self.serializer_class(instance=product , data=new_data_product)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data , status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request , product_id):
        product = get_object_or_404(Products,id=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   