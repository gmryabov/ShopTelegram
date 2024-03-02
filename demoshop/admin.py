from django.contrib import admin

from .models import *

admin.site.register(ContactInfo)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    verbose_name = 'Изображение'
    verbose_name_plural = 'Изображения'
    max_num = 10
    extra = 0
    can_delete = True


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'memory', 'price', 'category', 'tags',)
    list_filter = ('price', 'name')
    list_display_links = ('name',)
    list_editable = ('price', 'tags',)
    search_fields = ['name']
    search_help_text = 'Поиск по наименованию'
    list_per_page = 20
    actions = ['delete_selected']
    inlines = [ProductImageInline, ]


admin.site.register(Products, ProductAdmin)


class CreditChild(admin.StackedInline):
    model = CreditProgram


class CreditParent(admin.ModelAdmin):
    inlines = [CreditChild]


admin.site.register(CreditInfo, CreditParent)


class CategoryChild(admin.StackedInline):
    model = SubCategory


class CategoryFather(admin.ModelAdmin):
    inlines = [CategoryChild]
    list_display = ('id', 'title',)
    list_filter = ('id',)
    list_display_links = ('title',)


admin.site.register(Categories, CategoryFather)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'title', 'id', 'sort',)
    list_editable = ('sort', 'is_active')
    list_filter = ('sort',)
    search_fields = ('title',)
    list_display_links = ('title',)
    list_per_page = 20
    actions = ['delete_selected']

