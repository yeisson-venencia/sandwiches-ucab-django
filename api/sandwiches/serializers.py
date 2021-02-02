from rest_framework import serializers
from .models import Order, Sand_Ing, Sandwich, Size, Ingredient
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class Sand_IngSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)
    
    class Meta:
        model = Sand_Ing
        fields = '__all__'

class SandwichSerializer(serializers.ModelSerializer):
    ingredients = Sand_IngSerializer(many=True, read_only=True)
    size = SizeSerializer(many=False, read_only=True)
    class Meta:
        model = Sandwich
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    sandwiches = SandwichSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'