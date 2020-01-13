from django.contrib import admin
from .models import Car

# Register your models here.

class   CarAdmin(admin.ModelAdmin):
    list_display=('manufacturer', 'year', 'colour')

admin.site.register(Car, CarAdmin)