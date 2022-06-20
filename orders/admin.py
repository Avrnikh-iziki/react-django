from django.contrib import admin
from .models import Order ,ListOfOrders

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_id','username','email','phone_number','isTreated', 'total']
    list_filter=['placed_at']
    
@admin.register(ListOfOrders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','price','quantity']
   
    
   
