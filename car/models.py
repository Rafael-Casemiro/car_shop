from django.db import models
from user.models import User

class Car(models.Model):
        user = models.ForeignKey(to=User, on_delete=models.CASCADE)
        license_plate = models.CharField(max_length=20)
        model = models.CharField(max_length=20)
        brand = models.CharField(max_length=100)
        manufacturing_year = models.IntegerField()
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)

        class Meta:
                verbose_name = 'Car'
                verbose_name_plural = 'Cars'
        
        def __str__(self):
                return f'{self.model} {self.brand}'