from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
        list_display = ('id', 'user', 'license_plate', 'model', 'brand')
        list_filter = ('id', 'user', 'license_plate', 'model', 'brand')


admin.site.register(Car, CarAdmin)