from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',

        'GET /api/users',
        'GET /api/user/id',
        'PUT /api/update-user/id',
        'DELETE /api/delete-user/id',

        'GET /api/customers',
        'GET /api/customer/id',
        'PUT /api/update-customer/id',
        'DELETE /api/delete-customer/id',
    ]
    return Response(routes)

# USER VIEWS

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUserDetail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateUser(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('User was deleted!')

# CUSTOMER VIEWS

@api_view(['GET'])
def getCustomers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCustomerDetail(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateCustomer(request, pk):
    data = request.data
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response('Customer was deleted!')
