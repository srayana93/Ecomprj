from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')  # adjust fields as needed
    prepopulated_fields = {"slug": ("name",)}  # Ensure 'slug' is a valid field in your model

