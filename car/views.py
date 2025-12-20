from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car


def register_car(request):
        if request.method == 'POST':
                form = CarForm(request.POST)

                if form.is_valid():
                        car_instance = form.save(commit=False)
                        
                        car_instance.user = request.user
                        
                        if Car.objects.filter(license_plate=car_instance.license_plate).exists():
                                form.add_error('license_plate', 'Placa já cadastrada no sistema.')
                                return render(request, 'car/register.html', {'form': form})

                        car_instance.save()

                        return redirect('user:index')
        else:
                form = CarForm()
        
        return render(request, 'car/register_car.html', {'form': form})


def car_list(request):
        cars = Car.objects.all()

        return render(
                request,
                'car/list_car.html',
                {'cars': cars}
        )
        

