from django.db import models
from vehicle.models import Book
# Create your models here.


class Cleanliness(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    inside_tent = models.ImageField(upload_to="genie/cleanliness", blank=True)
    inside_car = models.ImageField(upload_to="genie/cleanliness", blank=True)
    outside_car = models.ImageField(upload_to="genie/cleanliness", blank=True)

    def __str__(self):
        return str(self.book.pk)


class VehiclePhoto(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    front = models.ImageField(upload_to="genie/vehicle_photo", blank=True)
    back = models.ImageField(upload_to="genie/vehicle_photo", blank=True)
    side1 = models.ImageField(upload_to="genie/vehicle_photo", blank=True)
    side2 = models.ImageField(upload_to="genie/vehicle_photo", blank=True)

    def __str__(self):
        return str(self.book.pk)


class PhotoId(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    id1 = models.ImageField(upload_to="genie/vehicle_photo", blank=True)
    id2 = models.ImageField(upload_to="genie/vehicle_photo", blank=True)
    id3 = models.ImageField(upload_to="genie/vehicle_photo", blank=True)
    id4 = models.ImageField(upload_to="genie/vehicle_photo", blank=True)
    id5 = models.ImageField(upload_to="genie/vehicle_photo", blank=True)

    def __str__(self):
        return str(self.book.pk)