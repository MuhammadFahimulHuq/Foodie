
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Customer(AbstractUser):
    address = models.TextField(max_length=200)
    phoneNo = models.CharField(max_length=20)
    accountCreated = models.DateTimeField(auto_now_add=True)
    profilePicture = models.ImageField(upload_to='static/customer_image', blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)

