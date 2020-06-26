from django.contrib import admin
from .models import Temperature

# Register your models here.

class Temp(admin.ModelAdmin):
    #해당 리스트는 반드시 class model과 같은
    list_display = ['humi', 'temp']

admin.site.register(Temperature, Temp)