from django.contrib import admin

from pages.models import Listing


class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Listing, ListingAdmin)
