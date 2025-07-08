from django.contrib import admin
from .models import CustomUser, Product, Category
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "first_name", "last_name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "featured"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
