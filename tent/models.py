from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TentCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tent_check")
    rod = models.BooleanField()
    mattress = models.BooleanField()
    zip = models.BooleanField()
    rain_cover = models.BooleanField()
    ladder = models.BooleanField()
    straps = models.BooleanField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class TentCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tent_cart")
    txnid = models.CharField(max_length=128, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username
