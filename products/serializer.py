from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products 
        fields=['id','name','price','description','image' ,'quantity','placed_at','updated_at']

