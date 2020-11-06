from django.contrib import admin
from home.models import Drinks, Foods, Deals, Post, Images


# Register your models here.

class DrinksAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', ]
    list_filter = ['title']
    readonly_fields = ('image_tag',)


class DealsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', ]
    list_filter = ['title']
    readonly_fields = ('image_tag',)


class FoodsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', ]
    list_filter = ['title']
    readonly_fields = ('image_tag',)


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category',]
#     list_filter = ['category']
#     inlines = [ProductImageInline]
#     readonly_fields=('image_tag',)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    list_filter = ['title']
    readonly_fields = ('image_tag',)


admin.site.register(Drinks, DrinksAdmin)
admin.site.register(Deals, DealsAdmin)
admin.site.register(Foods, FoodsAdmin)
admin.site.register(Post, PostAdmin)

# admin.site.register(Product, ProductAdmin)
