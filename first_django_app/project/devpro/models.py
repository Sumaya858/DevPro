from django.db import models
from token_auth.models import User
# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    owner = models.ForeignKey(User, related_name='itemuser', on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f'{self.name}'
    

class Whishlist(models.Model):
    wishtitle = models.CharField(max_length=300)
    link = models.CharField(max_length=1000)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.wishtitle


class Order(models.Model):
    email = models.EmailField()

class Product(models.Model):
    # ...
    pass

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('order', 'product')