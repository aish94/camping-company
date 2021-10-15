from django.db import models
from django.contrib.auth.models import User


class Pay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment")
    txnid = models.CharField(max_length=128, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    coupon = models.FloatField(blank=True, null=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    productinfo = models.CharField(max_length=32, default='car book')
    phone = models.BigIntegerField(blank=True, null=True)
    car_price = models.IntegerField(blank=True, null=True)
    person_price = models.IntegerField(blank=True, null=True)
    campkit = models.IntegerField(blank=True, null=True)
    gas_stove = models.IntegerField(blank=True, null=True)
    solar_power = models.IntegerField(blank=True, null=True)
    torch = models.IntegerField(blank=True, null=True)
    chair = models.IntegerField(blank=True, null=True)
    table = models.IntegerField(blank=True, null=True)
    air_mattress = models.IntegerField(blank=True, null=True)
    igst = models.FloatField(blank=True, null=True)
    convenient = models.FloatField(blank=True, null=True)
    shillong_transfer = models.IntegerField(blank=True, null=True)
    airport_transfer = models.IntegerField(blank=True, null=True)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username
