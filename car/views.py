from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
        

        return render(
                request,
                'car/car_details.html',
                {'car': car}
        )


@login_required(login_url='login')
def buy_car(request, id):
        car = get_object_or_404(Car, id=id)


        if car.user == request.user:
                messages.error(request, "Você não pode comprar seu próprio veículo.")
                return redirect('car:car_list')
        
        if car.buyer is not None:
                messages.error(request, "Este veículo já foi vendido.")
                return redirect('car:car_list')
        
        if request.method == 'POST':
                car.buyer = request.user
                car.save()

                messages.success(request, "Compra realizada com sucesso! Parabéns pelo novo carro.")
                return redirect('car:car_list')
        
        return render(request, 'car/confirm_purchase.html', {'car': car})

def my_cars(request):
        cars = Car.objects.filter(buyer=request.user).order_by('-created_at')
        paginator = Paginator(cars, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        context = {
                'page_obj': page_obj,
                'site_title': 'My Cars - ',
                'cars': cars
        }


        return render(
                request,
                'car/my_cars.html',
                context
        )

def my_cars_sold(request):
        cars = Car.objects.filter(user=request.user.id, buyer__isnull=False).order_by('-created_at')


        

        paginator = Paginator(cars, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        context = {
                'page_obj': page_obj,
                'site_title': 'My Cars - ',
                'cars': cars
        }


        return render(
                request,
                'car/my_cars_sold.html',
                context
        )