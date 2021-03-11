from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    description = models.TextField(max_length=200)


