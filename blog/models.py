from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=64)
    sub_heading = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    # tags = models.TextField() comments?? views/like??
    blog_images = models.ImageField(upload_to="blog_images", blank=True)
    blog_cover_images = models.ImageField(upload_to="blog_images", blank=True)
    created_date = models.DateField(auto_now_add=True)  # auto_now update every time save, auto now add only once
    created_time = models.TimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    slug = models.SlugField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.slug


class Image(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    heading = models.CharField(max_length=256, blank=True, null=True)
    blog_image1 = models.ImageField(upload_to="blog_image", blank=True)
    blog_image2 = models.ImageField(upload_to="blog_image", blank=True)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.blog.heading


class Form(models.Model):
    referral = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    driving = models.CharField(max_length=64)
    food = models.CharField(max_length=64)
    sleep = models.CharField(max_length=64)
    anything = models.CharField(max_length=64)

    def __str__(self):
        return self.email


def blog_pre_save_receiver(sender, instance, **kwargs):
    temp = ""
    title = instance.heading
    for x in title:
        if x == " ":
            temp += "-"
        elif x.isalnum():
            temp += x
    instance.slug = temp
    # slug cant have question marks boy


pre_save.connect(blog_pre_save_receiver, sender=Blog)
