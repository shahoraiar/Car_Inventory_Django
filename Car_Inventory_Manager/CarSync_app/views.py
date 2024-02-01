from django.shortcuts import render , redirect
from .forms import CarForm
from .models import CarModel

# Create your views here.
def home(request) : 
    return render(request,'index.html')

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car_instance = form.save(commit=False) 

            fuel_efficiency = request.POST.get('fuel_efficiency')
            battery_capacity = request.POST.get('battery_capacity')

            if fuel_efficiency:
                try:
                    car_instance.fuel_efficiency = float(fuel_efficiency)
                except ValueError:
                    form.add_error('fuel_efficiency', 'Invalid input. Please enter a valid number for Fuel Efficiency.')
            if battery_capacity:
                try:
                    car_instance.battery_capacity = float(battery_capacity)
                except ValueError:
                    form.add_error('battery_capacity', 'Invalid input. Please enter a valid number for Battery Capacity.')
            # Save the instance 
            car_instance.save()           
            form = CarForm()

            success_message = "Car added successfully."

            return render(request, 'car/car_form.html', {'form': form, 'success_message': success_message})

    else:
        form = CarForm()

    return render(request, 'car/car_form.html', {'form': form})

def show_car(request) : 
    cars = CarModel.objects.all()
    return render(request, 'car/show_car.html' , {'cars' : cars})