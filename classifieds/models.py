from django.contrib.auth.models import User
from django.db import models
import moneyed
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class City(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    state = models.CharField(max_length=2, blank=True, null=True, default=None)

    def __str__(self):
        return self.name.lower()

    class Meta:
        ordering = ['name']
        unique_together = (('name', 'state'),)


class Category(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.lower()

    class Meta:
        default_related_name = 'categories'


class SubCategory(models.Model):

    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.lower()

    @property
    def price_desc(self):
        return self.listings.order_by('-price')

    @property
    def price_asc(self):
        return self.listings.order_by('price')

    class Meta:
        ordering = ['name']
        default_related_name = 'subcategories'


class Listing(models.Model):

    title = models.CharField(max_length=300)
    body = models.TextField(max_length=2000)
    price = MoneyField(max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
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
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        default_related_name = 'listings'
