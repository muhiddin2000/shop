from django.contrib import admin
from .models import Category
# from modeltranslation.admin import TranslationAdmin


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
