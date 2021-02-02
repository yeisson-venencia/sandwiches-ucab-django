from rest_framework import serializers
from .models import Order, Sand_Ing, Sandwich, Size, Ingredient

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
class Sand_IngSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sand_Ing
        fields = '__all__'

class SandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandwich
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
