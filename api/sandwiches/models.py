from django.db import models
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=20)


class Size(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(decimal_places=2, max_digits=20)

class Ingredient(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(decimal_places=2, max_digits=20)

class Sandwich(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

class Sand_Ing(models.Model):
    rations = models.IntegerField()
    sandwich = models.ForeignKey(Sandwich, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

