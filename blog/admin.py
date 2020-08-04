from django.contrib import admin
from blog.models import (Blog, Image,
                         Form, EventCart)

# Register your models here.

admin.site.register(Blog)
admin.site.register(Image)
admin.site.register(Form)
admin.site.register(EventCart)
