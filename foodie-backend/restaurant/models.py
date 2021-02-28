from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    Restaurant_name = models.CharField(max_length=100)
    Restaurant_password = models.CharField(max_length=50)
    Restaurant_address = models.TextField(max_length=200)
    Restaurant_email = models.EmailField(max_length=62)
    Restaurant_description = models.TextField(max_length=200)
    Restaurant_phoneNo = models.CharField(max_length=20)
    Restaurant_accountCreated = models.DateTimeField(auto_now_add=True)
    Restaurant_categories = models.CharField(max_length=100)
    Restaurant_rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=1.0)
