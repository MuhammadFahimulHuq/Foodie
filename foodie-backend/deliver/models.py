from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Deliver(AbstractUser):
    nidNo = models.IntegerField(null=False, blank=False)
    phoneNo = models.CharField(max_length=20)
    accountCreated = models.DateTimeField(auto_now_add=True)
    profilePicture = models.ImageField(blank=True, null=True)
    dateOfBirth = models.DateField(blank=False)
    address = models.TextField(max_length=200)

