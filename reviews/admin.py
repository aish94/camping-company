from django.contrib import admin
from reviews.models import DestinationReview,BlogReview

# Register your models here.

admin.site.register(DestinationReview)
admin.site.register(BlogReview)