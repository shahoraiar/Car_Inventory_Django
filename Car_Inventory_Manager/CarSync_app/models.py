from django.db import models

# Create your models here.
class CarModel(models.Model):
    CAR_TYPE_CHOICES = [
        ('Electric', 'Electric'),
        ('Gas', 'Gas'),
    ]

    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    car_type = models.CharField(max_length=8, choices=CAR_TYPE_CHOICES)
    battery_capacity = models.FloatField(null=True, blank=True)
    fuel_efficiency = models.FloatField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year}-{self.name}-{self.model}"

