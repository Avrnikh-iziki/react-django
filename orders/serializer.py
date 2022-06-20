from rest_framework import serializers
from .models import Order , ListOfOrders


class SerializerListOfOrders(serializers.ModelSerializer):

    class Meta:
        model=ListOfOrders
        fields = ['name', 'price', 'quantity']
     

class OrdersSerializer(serializers.ModelSerializer):
    listorder = SerializerListOfOrders(many=True)

    class Meta:
        model = Order 
        fields = ['id','customer_id','username','email','phone_number','isTreated', 'total', 'placed_at','listorder']
       
            
    def create(self, validated_data):
        orders_data = validated_data.pop("listorder")
        order= Order.objects.create(**validated_data)
        for order_data in orders_data:
            ListOfOrders.objects.create(order=order, **order_data)
        return order


    def update(self, instance, validated_data):
        instance.isTreated = True
        instance.save()
        return instance
   