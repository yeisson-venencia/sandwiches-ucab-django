from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,  name='api-overview'),
    path('ingredients-list/', views.ingredient_list,  name='api-ingredient-list'),
]