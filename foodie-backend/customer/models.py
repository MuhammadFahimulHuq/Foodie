from django.db import models
from djangoratings.fields import RatingField

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_password = models.CharField(max_length=50)
    customer_address = models.TextField(max_length=200)
    customer_email = models.EmailField(max_length=62)
    customer_phoneNo = models.CharField(max_length=20)
    customer_accountCreated = models.DateTimeField(auto_now_add=True)
    customer_profilePicture = models.ImageField(blank=True, null=True)
    customer_dateOfBirth = models.DateTimeField(blank=False)
    customer_rating = RatingField(range=5)