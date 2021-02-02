from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,  name='api-overview'),
    path('ingredient-list/', views.ingredient_list,  name='api-ingredient-list'),
    path('size-list/', views.size_list,  name='api-size-list'),
    path('register-order/', views.register_order, name='api-register-order')
]