from django.shortcuts import render , get_object_or_404
from rest_framework import  generics, status
from rest_framework.response import Response
from . import serializer
from .models import Order 
from rest_framework.permissions import IsAdminUser , IsAuthenticated


class OrdersViews(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializer.OrdersSerializer
    queryset = Order.objects.all()

    def get(self , request):
        data = Order.objects.filter(isTreated=False).order_by('placed_at').reverse()
        serializer =  self.serializer_class(instance=data, many=True)
        return Response(data={ "order": serializer.data } , status=status.HTTP_200_OK)

    def post(self , request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data =serializer.data , status=status.HTTP_201_CREATED)
        return Response(data = serializer.errors , status= status.HTTP_400_BAD_REQUEST)

class ManageOrderViews(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class=serializer.OrdersSerializer
    queryset=Order.objects.all()


    def put(self, request, order_id):
        order=get_object_or_404(Order,pk=order_id)
        treated = request.data
        serializer=self.serializer_class(instance=order , data=treated)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data , status=status.HTTP_200_OK)
        return Response(data=serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(sself, request,order_id):
        order = get_object_or_404(Order,id=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustumerOrdesViews(generics.GenericAPIView):
    serializer_class = serializer.OrdersSerializer
    queryset=Order.objects.all()
    permission_classes = [IsAuthenticated]
    def get (self, request, customer_id):
        data = Order.objects.filter(customer_id=customer_id , isTreated =False)
        serializer =  self.serializer_class(instance=data, many=True)
        return Response(data=serializer.data , status=status.HTTP_200_OK)
    
