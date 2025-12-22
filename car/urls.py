from django.urls import path, include
from .views import register_car, car_list, car_details

app_name = 'car'

urlpatterns = [
    path('register/', register_car, name='register_car'),
    path('list/', car_list, name='car_list'),
    path('details/<int:car_id>/', car_details, name='car_details')
]
