from classifieds.models import Listing, City, Category, SubCategory
from django.contrib import admin


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'body', 'price', 'phone_num',
                    'city', 'image', 'created_at')
    list_filter = ['created_at', 'city']
    search_fields = ['title', 'body']
    actions = ['archive_listings']

    def archive_listings(self, request, queryset):
        queryset.update(archived=True)

    archive_listings.short_description = "Archive Listings"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'pk')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')