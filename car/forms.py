from django import forms
from .models import Car

class CarForm(forms.ModelForm):
        picture =  forms.ImageField(
                widget=forms.FileInput(
                        attrs={
                                'accept': 'image/*',
                        }
                ),
                required=True
        )
        class Meta:
                model = Car
                fields = ['license_plate', 'model', 'brand', 'manufacturing_year', 'price', 'picture']
                # Você pode definir os labels aqui ou diretamente no Model
                labels = {
                'license_plate': 'Placa',
                'model': 'Modelo',
                'brand': 'Marca',
                'manufacturing_year': 'Ano de Fabricação',
                'price': 'Preço'
                }