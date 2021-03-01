from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import RestaurantSerializer
from .models import Restaurant


# FETCH ALL RESTAURANT
@api_view(['GET'])
def restaurantLists(request):
    restaurant = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurant, many=True)
    return Response(serializer.data)


# FETCH ONE RESTAURANT THROUGH ID
def restaurantList(request,pk):
    restaurant = Restaurant.objects.get(id=pk)
    serializer = RestaurantSerializer(restaurant, many=False)
    return Response(serializer.data)


# CREATE A RESTAURANT
@api_view(['POST'])
def createRestaurant(request):
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#UPDATE A EXISITING RESTAURANT THROUGH ID
@api_view(['POST'])
def updateRestaurant(request,pk):
    restaurant = Restaurant.objects.get(id=pk)
    serializer = RestaurantSerializer(instance=restaurant, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#DELETE A RESTAURANT
@api_view(['DELETE'])
def deleteRestaurant(request,pk):
    restaurant =Restaurant.objects.get(id=pk)
    restaurant.delete()
    return Response('Deleted')