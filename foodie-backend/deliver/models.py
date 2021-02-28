from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Deliver(models.Model):
    deliver_name = models.CharField(max_length=100)
    deliver_password = models.CharField(max_length=50)
    deliver_nidNo = models.IntegerField(null=False, blank=False)
    deliver_email = models.EmailField(max_length=62)
    deliver_phoneNo = models.CharField(max_length=20)
    deliver_accountCreated = models.DateTimeField(auto_now_add=True)
    deliver_profilePicture = models.ImageField(blank=True, null=True)
    deliver_dateOfBirth = models.DateTimeField(blank=False)
    deliver_address = models.TextField(max_length=200)
    deliver_rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=1.0)
