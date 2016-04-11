from classifieds.models import Listing, City, Category, SubCategory
from django.contrib import admin


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'body', 'price', 'phone_num',
                    'city', 'image', 'created_at')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')