from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Slider)
admin.site.register(Ad)
admin.site.register(Brand)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Wishlist)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "labels", "brand")
    list_filter = ("category", "labels", "status")
    search_fields = ("name", "description", "category", "brand")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("username", "slug", "quantity", "total", "checkout")
    list_filter = ("checkout", "date")
    search_fields = ("username",)
