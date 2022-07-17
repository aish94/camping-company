from django.urls import path
from equipment.views import (equipment_create_check,
                             equipment_update_check,
                             inventory_create,
                             inventory_update)

app_name = "equipment"

urlpatterns = [
    path('<int:pk>/create', equipment_create_check, name="equipment_create_check"),
    path('<int:pk>/update', equipment_update_check, name="equipment_update_check"),
    path('<int:pk>/inventory_create', inventory_create, name="inventory_create"),
    path('<int:pk>/inventory_update', inventory_update, name="inventory_update"),

]
