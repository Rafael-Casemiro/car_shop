from django import forms
from .models import Car

class CarForm(forms.ModelForm):
        class Meta:
                model = Car
                fields = ['license_plate', 'model', 'brand', 'manufacturing_year', 'price']
                # Você pode definir os labels aqui ou diretamente no Model
                labels = {
                'license_plate': 'Placa',
                'model': 'Modelo',
                'brand': 'Marca',
                'manufacturing_year': 'Ano de Fabricação',
                'price': 'Preço'
                }