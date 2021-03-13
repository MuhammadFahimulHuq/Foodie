from rest_framework import serializers
from .models import Dishes

class DishesSerializer(serializers.ModelSerializer):
    class meta:
        model = Dishes
        field=['__all__']
