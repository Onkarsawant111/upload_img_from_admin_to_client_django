from django.contrib import admin
from .models import Picture

# Register your models here.
class Adminpicture(admin.ModelAdmin):
    list_display = ['id', 'img']

admin.site.register(Picture, Adminpicture)