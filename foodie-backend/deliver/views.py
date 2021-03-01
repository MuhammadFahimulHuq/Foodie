from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import DeliverSerializer
from .models import Deliver


# FETCH ALL DELIVER
@api_view(['GET'])
def deliverLists(request):
    deliver = Deliver.objects.all()
    serializer = DeliverSerializer(deliver, many=True)
    return Response(serializer.data)


# FETCH ONE DELIVER THROUGH ID
def deliverList(request,pk):
    customer = Deliver.objects.get(id=pk)
    serializer = DeliverSerializer(deliver, many=False)
    return Response(serializer.data)


# CREATE A DELIVER
@api_view(['POST'])
def createDeliver(request):
    serializer = DeliverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#UPDATE A EXISITING DELIVER THROUGH ID
@api_view(['POST'])
def updateDeliver(request,pk):
    deliver = Deliver.objects.get(id=pk)
    serializer = DeliverSerializer(instance=deliver, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#DELETE A DELIVER
@api_view(['DELETE'])
def deleteDeliver(request,pk):
    deliver = Deliver.objects.get(id=pk)
    deliver.delete()
    return Response('Deleted')