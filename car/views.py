from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import CarForm
from .models import Car


def register_car(request):
        if request.method == 'POST':
                form = CarForm(request.POST, request.FILES)

                if form.is_valid():
                        car_instance = form.save(commit=False)
                        
                        car_instance.user = request.user
                        
                        if Car.objects.filter(license_plate=car_instance.license_plate).exists():
                                form.add_error('license_plate', 'Placa já cadastrada no sistema.')
                                return render(request, 'car/register.html', {'form': form})

                        car_instance.save()

                        return redirect('car:car_list')
        else:
                form = CarForm()
        
        return render(request, 'car/register_car.html', {'form': form})


def car_list(request):
        cars = Car.objects.filter(buyer=None).order_by('-created_at')
        paginator = Paginator(cars, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
                'page_obj': page_obj,
                'site_title': 'Cars - ',
                'cars': cars
        }

        return render(
                request,
                'car/car_list.html',
                context
        )
        

def car_details(request, car_id):
        car = get_object_or_404(Car, pk=car_id)
        
        user = request.user

        context = {
                'car': car,
                'vendedor': user
        }

        return render(
                request,
                'car/car_details.html',
                {'car': car}
        )