from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dishes
from .serializer import DishesSerializer


# GET ALL THE DISHES
@api_view(['GET'])
def dishesList(request):
    dishes = Dishes.objects.all()
    serializer = DishesSerializer(dishes, many=True)
    return Response(serializer.data)


# CREATE A DISH
@api_view(['POST'])
def createDishes(request):
    serializer = DishesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET A DISH BY ID
def dishesById(request, pk):
    dishes = Dishes.objects.get(id=pk)
    serializer = DishesSerializer(dishes, many=False)
    return Response(serializer.data)


# DELETE A DISH
@api_view(['DELETE'])
def deleteDishes(request, pk):
    dishes = Dishes.objects.get(id=pk)
    dishes.delete()
    return Response('Deleted')
