from django.contrib import admin
from .models import TestImage

# Register your models here.
@admin.register(TestImage)
class TestImageAdmin(admin.ModelAdmin):
    list_display = ("name", "image")