from django.urls import path, include
from .views import register_car, car_list, car_details, buy_car, my_cars, my_cars_sold

app_name = 'car'

urlpatterns = [
    path('register/', register_car, name='register_car'),
    path('list/', car_list, name='car_list'),
    path('my_cars/', my_cars, name='my_cars'),
    path('my_cars_sold/', my_cars_sold, name='my_cars_sold'),
    path('details/<int:car_id>/', car_details, name='car_details'),
    path('buy/<int:id>/', buy_car, name='buy_car')
]
