from django.db import models
from dishes.models import Dishes


# Create your models here.
class AddToCart(models.Model):
    Dishes = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    SubTotal = models.FloatField()
    TotalBill = models.FloatField()
