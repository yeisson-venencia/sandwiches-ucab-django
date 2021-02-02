from django.contrib import admin

from .models import Order, Size, Ingredient, Sandwich, Sand_Ing, User

# Register your models here.
admin.site.register(Order)
admin.site.register(Size)
admin.site.register(Ingredient)
admin.site.register(Sandwich)
admin.site.register(Sand_Ing)
admin.site.register(User)