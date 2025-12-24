from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
        list_display = ('id', 'user', 'license_plate', 'model', 'brand', 'created_at', 'update_at')
        list_filter = ('id', 'user', 'license_plate', 'model', 'brand')


admin.site.register(Car, CarAdmin)