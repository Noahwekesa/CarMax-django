from django.contrib import admin
from users.models import Location, Profile


class LocationAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'bio', 'phone_number', 'location']


admin.site.register(Profile, ProfileAdmin)

admin.site.register(Location, LocationAdmin)
