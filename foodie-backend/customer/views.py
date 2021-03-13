from rest_framework import permissions, status
from rest_framework.permissions import AllowAny

from .models import Customer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from customer.serializer import CustomerSerializer


# FETCH ALL CUSTOMERS
@api_view(['GET'])
def customerLists(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)


# FETCH ONE CUSTOMER THROUGH ID
def customerList(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


# CREATE A CUSTOMER
@api_view(['POST'])
@permission_classes([AllowAny])
def createCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# UPDATE A EXISITING CUSTOMER THROUGH ID
@api_view(['POST'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# DELETE A CUSTOMER
@api_view(['DELETE'])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response('Deleted')


