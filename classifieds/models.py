from django.contrib.auth.models import User
from django.db import models
import moneyed
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class City(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name.lower()


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.lower()


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.lower()

    @property
    def price_desc(self):
        return self.listing_set.order_by('-price')

    @property
    def price_asc(self):
        return self.listing_set.order_by('price')


class Listing(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=2000)
    price = MoneyField(max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True,
                             related_name="listings")
    phone_num = PhoneNumberField(null=True, blank=True,
                                 verbose_name="Phone Number",
                                 help_text="+1(555)555-5555 format")
    city = models.ForeignKey(City)
    image = models.ImageField(upload_to='listing_picture/', null=True,
                              blank=True,
                              default='listing_picture/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    subcategory = models.ForeignKey(SubCategory)

    def __str__(self):
        return self.title
