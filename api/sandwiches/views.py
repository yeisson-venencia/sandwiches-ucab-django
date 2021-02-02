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

@api_view(['POST'])
def register_order(request):

    price_order = 0
    for r in request.data['sandwiches']:
        price_sandwich = float(r['size']['price'])
        for i in r['ingredients']:
            price_sandwich += float(i['price']) # *float(i['rations'])
        r['price'] = price_sandwich
        price_order += price_sandwich
    request.data['price'] = price_order

    order = Order.objects.create(price=request.data['price'])

    for s in request.data['sandwiches']:

        sandwich = Sandwich.objects.create(order=order, size=Size.objects.get(id=s['size']['id']), price=s['price'])

        for i in s['ingredients']:

            Sand_Ing.objects.create(
                sandwich=sandwich, 
                ingredient=Ingredient.objects.get(id=i['id']),
                rations=i['rations']
            )


    
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_orders(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def get_all_sandwich_size(request):
    sandwich = Sandwich.objects.filter(size=Size.objects.get(id=request.data['id']))
    serializer = SandwichSerializer(sandwich, many=True)
    return Response(serializer.data)