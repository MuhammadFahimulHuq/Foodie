from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class Deliver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    nidNo = models.IntegerField(null=False, blank=False)
    profilePicture = models.ImageField(blank=True, null=True)



