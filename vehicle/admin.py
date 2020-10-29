from django.contrib import admin
from vehicle.models import (VehicleCheck, Definition,
                            Book, Region)

# Register your models here.

admin.site.register(VehicleCheck)
admin.site.register(Definition)
admin.site.register(Book)
admin.site.register(Region)
