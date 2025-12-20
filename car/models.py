from django.db import models
from user.models import User

class Car(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendedor')
        buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comprador')
        license_plate = models.CharField(max_length=20, unique=True)
        model = models.CharField(max_length=20)
        brand = models.CharField(max_length=100)
        manufacturing_year = models.IntegerField()
        price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)

        class Meta:
                verbose_name = 'Car'
                verbose_name_plural = 'Cars'
        
        def __str__(self):
                return f'{self.model} {self.brand} - R$ {self.price}'
        
        @property
        def is_solid(self):
                return self.buyer is not None