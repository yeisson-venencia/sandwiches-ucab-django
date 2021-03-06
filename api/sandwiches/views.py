import datetime

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order, Sand_Ing, Sandwich, Size, Ingredient, User
from .serializers import OrderSerializer, Sand_IngSerializer, SandwichSerializer, SizeSerializer, IngredientSerializer, UserSerializer

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
            price_sandwich += float(i['price']) *float(i['rations'])
        r['price'] = price_sandwich
        price_order += price_sandwich
    request.data['price'] = price_order

    user = None
    try:
        user = User.objects.get(id=request.data['user']['id'])
    except:
        user = User.objects.create(
            document=request.data['user']['document'],
            first_name=request.data['user']['first_name'],
            last_name=request.data['user']['last_name']
        )

    order = Order.objects.create(price=request.data['price'], user=user)

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

@api_view(['POST'])
def get_orders_day(request):
    date = datetime.datetime.strptime(request.data['date'], '%Y-%m-%d')
    order = Order.objects.filter(date__date = date)
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def get_all_sandwich_user(request):
    order = Order.objects.filter(user = User.objects.get(id=request.data['id']))
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def get_sandwich_ingredient(request):
    ingredient = Ingredient.objects.get(id = request.data['ingredient']['id'])
    sand_ingres = ingredient.ingredient.all()
    sandwiches = set()
    for si in sand_ingres:
        sandwiches.add(si.sandwich)
    serializer = SandwichSerializer(sandwiches, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def verify_user(request):
    try:
        user = User.objects.get(document = request.data['document'])
        serializer =  UserSerializer(user)
        return Response(serializer.data)
    except:
        return JsonResponse({})
    

