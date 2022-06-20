from django.db import models

class Products(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
    image=models.CharField(blank=True, null=True , max_length=500)
    placed_at=models.DateTimeField( auto_now_add=True ,null=False)
    updated_at=models.DateTimeField(auto_now=True ,null=False)


    def __str__(self):
        return f"<Order  by {self.name}>"



