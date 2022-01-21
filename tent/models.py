from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


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
    igst = models.FloatField(blank=True, null=True)
    convenient = models.FloatField(blank=True, null=True)
    created = models.DateField(auto_now=True)
    coupon = models.FloatField(blank=True, null=True)
    ladder = models.FloatField(blank=True, null=True)
    shipping = models.FloatField(blank=True, null=True)
    tent = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Tent(models.Model):
    slug = models.SlugField(max_length=40, blank=True, null=True)
    main_tent_image = models.ImageField(upload_to='tent', blank=True)

    name = models.CharField(max_length=128, blank=True, null=True, unique=True)
    name_extended = models.CharField(max_length=128, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField()
    warranty = models.TextField()
    features = models.TextField()
    telescopic_ladder = models.IntegerField(blank=True, null=True)

    sleeping_capacity = models.CharField(max_length=128, blank=True, null=True)
    dimentions_closed = models.CharField(max_length=128, blank=True, null=True)
    weight = models.CharField(max_length=128, blank=True, null=True)
    static_weight_capacity = models.CharField(max_length=128, blank=True, null=True)
    minimum_bar_spread = models.CharField(max_length=128, blank=True, null=True)
    base_construction = models.CharField(max_length=128, blank=True, null=True)
    canopy_fabric = models.CharField(max_length=128, blank=True, null=True)
    internal_frame = models.CharField(max_length=128, blank=True, null=True)
    mosquito_screens = models.CharField(max_length=128, blank=True, null=True)
    seasons = models.CharField(max_length=128, blank=True, null=True)
    colors = models.CharField(max_length=128, blank=True, null=True)

    model_number = models.CharField(max_length=128, blank=True, null=True)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return f'Tent name - {self.name}'


class TentImage(models.Model):
    tent = models.ForeignKey(Tent, on_delete=models.CASCADE, related_name="tent")
    image_url = models.ImageField(upload_to='tent')

    def __str__(self):
        return f'{self.tent.name} - image'


def tent_pre_save_receiver(sender, instance, **kwargs):
    instance.slug = "".join(["-" if x is " " else x for x in instance.name])


pre_save.connect(tent_pre_save_receiver, sender=Tent)
