from django.db import models
from django.contrib.auth.models import User
from destination.models import Destination
from django.db.models.signals import pre_save


class DestinationReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_user")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="review_destination")
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    rating = models.IntegerField()
    rated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' give ' + str(self.rating)


def destination_review_pre_save_receiver(sender, instance, **kwargs):
    des = Destination.objects.get(slug=instance.destination.slug)
    des.total_rating += int(instance.rating)
    des.save()


pre_save.connect(destination_review_pre_save_receiver, sender=DestinationReview)