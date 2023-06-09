from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @property
    def item_count(self):
        items = self.orderitem_set.all()
        total = sum([item.quantity for item in items])
        return total

    @property
    def all_summa(self):
        items = self.orderitem_set.all()
        total = sum([item.summa for item in items])
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.order} ning xaridi!"

    @property
    def summa(self):
        total = self.product.cost * self.quantity
        return total
