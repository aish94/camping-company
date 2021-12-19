from django.contrib import admin
from .models import (TentCheck, TentCart, Tent, TentImage)
# Register your models here.

admin.site.register(TentCheck)
admin.site.register(TentCart)
admin.site.register(Tent)
admin.site.register(TentImage)