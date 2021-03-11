from rest_framework import serializers

from user.serializer import UserSerializer
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Restaurant
        fields = ['user', 'description']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        restaurant, created = Restaurant.objects.update_or_create(user = user,description=validated_data.pop('description'))
        return restaurant
