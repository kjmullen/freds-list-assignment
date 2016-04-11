from classifieds.models import City
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    user = models.OneToOneField(User, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    @property
    def city_name_and_id(self):
        return [self.city.name, self.city_id]