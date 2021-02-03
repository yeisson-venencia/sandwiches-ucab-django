from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    document = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Order(models.Model):
    date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

class Size(models.Model):
    name = models.CharField(max_length=80, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=80, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=True)

    def __str__(self) -> str:
        return self.name

class Sandwich(models.Model):
    order = models.ForeignKey(Order, related_name='sandwiches', on_delete=models.CASCADE, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)

class Sand_Ing(models.Model):
    rations = models.IntegerField()
    sandwich = models.ForeignKey(Sandwich, related_name='ingredients', on_delete=models.CASCADE, blank=True)
    ingredient = models.ForeignKey(Ingredient, related_name='ingredient', on_delete=models.CASCADE, blank=True)
