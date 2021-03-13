from rest_framework import serializers

from dishes.serializer import DishesSerializer
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=5)
    dishes = DishesSerializer(required=False)
    class Meta:
        model = Category
        fields = ['name']
