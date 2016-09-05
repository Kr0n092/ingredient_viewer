from django.contrib import admin


# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    admin.site.register(Product)