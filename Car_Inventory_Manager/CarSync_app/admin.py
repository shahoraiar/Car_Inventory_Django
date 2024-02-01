from django.contrib import admin
from .models import CarModel
# Register your models here.
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'year', 'car_type', 'battery_capacity', 'fuel_efficiency', 'create_at')

admin.site.register(CarModel, CarModelAdmin)
