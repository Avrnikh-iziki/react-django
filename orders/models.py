
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Order(models.Model):
    customer_id=models.ForeignKey(User ,   on_delete=models.CASCADE )
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    total=models.FloatField()
    isTreated=models.BooleanField(default=False)
    placed_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"<Order  by {self.username}>"


class ListOfOrders(models.Model):
    order= models.ForeignKey(Order, related_name='listorder', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
