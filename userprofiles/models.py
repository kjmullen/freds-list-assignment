from classifieds.models import City
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Profile(models.Model):

    user = models.OneToOneField(User, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    @property
    def city_name_and_id(self):
        return [self.city.name, self.city_id]

    def reset_token(self):
        token = Token.objects.get(user=self.user)
        token.delete()
        Token.objects.create(user=self.user)
        # self.user.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)