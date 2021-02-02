from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,  name='api-overview'),
    path('ingredient-list/', views.ingredient_list,  name='api-ingredient-list'),
    path('size-list/', views.size_list,  name='api-size-list'),
    path('sandwich-list/', views.sandwich_list,  name='api-sandwich-list'),
    path('order-list/', views.order_list,  name='api-order-list'),
    path('create-order/', views.create_order,  name='api-create-order'),
]