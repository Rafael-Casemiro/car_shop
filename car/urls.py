from django.urls import path, include
from .views import register_car

app_name = 'car'

urlpatterns = [
    path('register/', register_car, name='register_car')
]
