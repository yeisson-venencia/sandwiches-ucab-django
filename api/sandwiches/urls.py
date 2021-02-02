from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,  name='api-overview'),
    path('ingredient-list/', views.ingredient_list,  name='api-ingredient-list'),
    path('size-list/', views.size_list,  name='api-size-list'),
    path('register-order/', views.register_order, name='api-register-order'),
    path('get-orders/', views.get_all_orders, name='api-get-orders'),
    path('get-sandwiches-ingredient/', views.get_sandwich_ingredient, name='api-get-sandwiches-ingredient'),
    path('get-all-sandwich-size/',views.get_all_sandwich_size, name='get-all-sandwich-size'),
    path('get-orders-day/', views.get_orders_day, name='api-get-orders-day'),
]