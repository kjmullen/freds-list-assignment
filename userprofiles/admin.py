from django.contrib import admin
from userprofiles.models import Profile


@admin.register(Profile)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'email')
