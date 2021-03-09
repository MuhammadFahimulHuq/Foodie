from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Restaurant_description = models.TextField(max_length=200)
    Restaurant_categories = models.CharField(max_length=100)
    Restaurant_rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=1.0)
