from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CustomerSerializer
from .models import Customer


# FETCH ALL CUSTOMERS
@api_view(['GET'])
def customerLists(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)


# FETCH ONE CUSTOMER THROUGH ID
def customerList(request,pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


# CREATE A CUSTOMER
@api_view(['POST'])
def createCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#UPDATE A EXISITING CUSTOMER THROUGH ID
@api_view(['POST'])
def updateCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#DELETE A CUSTOMER
@api_view(['DELETE'])
def deleteCustomer(request,pk):
    customer =Customer.objects.get(id=pk)
    customer.delete()
    return Response('Deleted')