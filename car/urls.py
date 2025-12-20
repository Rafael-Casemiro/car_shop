from django.urls import path, include
from .views import register_car, car_list

app_name = 'car'

urlpatterns = [
    path('register/', register_car, name='register_car'),
    path('list/', car_list, name='car_list')
]
