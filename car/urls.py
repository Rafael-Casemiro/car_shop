from django.urls import path, include
from .views import register_car, car_list, car_details, buy_car, my_cars, my_cars_sold

app_name = 'car'

urlpatterns = [
    path('car/register/', register_car, name='register_car'),
    path('', car_list, name='car_list'),
    path('car/my_cars/', my_cars, name='my_cars'),
    path('car/my_cars_sold/', my_cars_sold, name='my_cars_sold'),
    path('car/details/<int:car_id>/', car_details, name='car_details'),
    path('car/buy/<int:id>/', buy_car, name='buy_car')
]
