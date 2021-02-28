from django.db import models


# Create your models here.
class Dishes(models.Model):
    Dishes_ingredient = models.TextField(max_length=200)
    Dishes_name = models.CharField(max_length=100)
    Dishes_price = models.FloatField()
    Dishes_picture = models.ImageField(blank=True, null=True)
    Dishes_discount = models.FloatField()
    Dishes_category = models.CharField(max_length=100)
