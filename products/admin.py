from django.contrib import admin
from .models import Products
@admin.register(Products)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','quantity','description','image']
    list_filter= ['placed_at', 'name','price']
