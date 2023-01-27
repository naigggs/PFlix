from django.http import JsonResponse
# from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import render

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',

        '/api/products/upload/',

        '/api/products/<id>/reviews/',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>',

        '/api/directors/',
        '/api/directors/<id>/',
        '/api/directorsproducts/<str:pk>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getDirectors(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDirector(request, pk):
    director = Director.objects.get(_id=pk)
    serializer = DirectorSerializer(director, many=False)
    return Response(serializer.data)    

@api_view(['GET'])
def getDirectorProducts(request, pk):
    products = Product.objects.filter(director = pk)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)