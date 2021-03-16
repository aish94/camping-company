from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class VehicleCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="vehicle_check",
                             null=True, blank=True)
    engine_oil_level = models.PositiveIntegerField()
    brake_fluid_level = models.PositiveIntegerField()
    water_level = models.PositiveIntegerField()
    windscreen_washer = models.BooleanField()
    seatbelts_check = models.BooleanField()
    parking_brake = models.BooleanField()
    clutch_gearshift = models.BooleanField()
    burning_smell = models.BooleanField()
    steering_alignment = models.BooleanField()
    dashboard = models.BooleanField()
    check_lights = models.BooleanField()
    horn = models.BooleanField()
    tyres = models.BooleanField()
    leakage = models.BooleanField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Definition(models.Model):
    car_name = models.CharField(max_length=64, blank=True, null=True)
    seat = models.CharField(max_length=12, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    color = models.CharField(max_length=12, blank=True, null=True)
    car_image = models.ImageField(upload_to="cars", blank=True, null=True)
    price = models.IntegerField()
    drive_train = models.CharField(max_length=64, blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.car_name


class Region(models.Model):
    cars = models.ManyToManyField(Definition, related_name="Region")
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE, null=True, blank=True)
    check_in_date = models.DateField(blank=True, null=True)
    check_out_date = models.DateField(blank=True, null=True)
    duration = models.IntegerField()
    txnid = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return str(self.check_in_date)+" "+str(self.check_out_date)+" "+self.definition.color
