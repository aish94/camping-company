from django.db import models
from django.contrib.auth.models import User

# Create your models here.

lead_status = (
    ("Lead Closed", "Lead Closed"),
    ("Follow Up", "Follow Up"),
)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_check", null=True)
    phone = models.BigIntegerField(null=True, blank=True)
    license_number = models.CharField(null=True, blank=True, max_length=128)
    city = models.CharField(null=True, blank=True, max_length=64)
    address = models.CharField(null=True, blank=True, max_length=256)
    nickname = models.CharField(null=True, blank=True, max_length=64)
    about = models.TextField(null=True, blank=True)
    terms_condition = models.BooleanField(default=False)
    lead_status = models.CharField(default="Follow Up", blank=True, max_length=128, null=True, choices=lead_status)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    people = models.CharField(max_length=64)
    companion = models.CharField(max_length=64)
    expectations = models.CharField(max_length=64)
    overlanding = models.CharField(max_length=64)
    itinerary = models.CharField(max_length=64)

    def __str__(self):
        return self.user.username
