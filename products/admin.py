from django.contrib import admin

# Register your models here.
from .models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_show','name','category','cost','discount']
    list_filter = ['category','discount']
    list_editable = ['name','category','cost','discount']
    search_fields = ['name','cost','description','discount']
    list_per_page = 10