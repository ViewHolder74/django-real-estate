from django.contrib import admin

from .models import Property, PropertyViews


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "advert_type", "property_type"]
    list_filter = ["advert_type", "property_type"]


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyViews)
