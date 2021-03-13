from django.db import models


# Create your models here.
from dishes.models import Dishes


class Category(models.Model):
    name = models.CharField(max_length=100)
    dishes = models.ForeignKey(Dishes,on_delete=models.CASCADE,null=True,blank=True)