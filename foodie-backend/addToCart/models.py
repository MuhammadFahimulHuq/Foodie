from django.db import models
from dishes.models import Dishes
from customer.models import Customer


# Create your models here.
class AddToCart(models.Model):
    Dishes = models.ManyToManyField(Dishes)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    SubTotal = models.FloatField()
    TotalBill = models.FloatField()

