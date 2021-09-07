from django.contrib import admin
from .models import (Destination, Map, Region,
                     Amenity, Activity,Image,
                     Detail, Circuit, Booking,
                     Feature, Experience,
                     PaymentCampsite,Pricing,Experiences)
# Register your models here.

admin.site.register(Destination)
admin.site.register(Map)
admin.site.register(Region)
admin.site.register(Amenity)
admin.site.register(Activity)
admin.site.register(Image)
admin.site.register(Detail)
admin.site.register(Circuit)
admin.site.register(Booking)
admin.site.register(Feature)
admin.site.register(Experience)
admin.site.register(PaymentCampsite)
admin.site.register(Pricing)
admin.site.register(Experiences)

