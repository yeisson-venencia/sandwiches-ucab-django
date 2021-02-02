from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order, Sand_Ing, Sandwich, Size, Ingredient
from .serializers import OrderSerializer, Sand_IngSerializer, SandwichSerializer, SizeSerializer, IngredientSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Example' : '/example/',
        'Create': '/create/',
        'Update': '/update/',
        'Delete': '/delete/',
    }

    return Response(api_urls)

@api_view(['GET'])
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def size_list(request):
    sizes = Size.objects.all()
    serializer = SizeSerializer(sizes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sandwich_list(request):
    sandwiches = Sandwich.objects.all()
    serializer = SandwichSerializer(sandwiches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_order(request):
    print('holaaaa')
    print(request.data)
    return Response('OK')
