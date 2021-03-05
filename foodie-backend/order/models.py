from django.db import models
from addToCart.models import AddToCart
from deliver.models import Deliver
from restaurant.models import Restaurant

# Create your models here.
class Order(models.Model):
    Order_Date = models.DateField(auto_now_add=True)
    Deliver_id = models.ForeignKey(Deliver,on_delete=models.CASCADE)
    AddToCart_id = models.OneToOneField(AddToCart,on_delete=models.CASCADE)
    Restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

