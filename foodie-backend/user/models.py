from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    address = models.TextField(max_length=200)
    phoneNo = models.CharField(max_length=20)
    accountCreated = models.DateTimeField(auto_now_add=True)
    dateOfBirth = models.DateField(blank=True, null=True)
