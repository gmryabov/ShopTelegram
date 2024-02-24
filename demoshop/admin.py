from django.contrib import admin
from .models import *

admin.site.register(Banner)
admin.site.register(PromoBlock)
admin.site.register(ContactInfo)

class ProductImageInline(admin.TabularInline):
  model = ProductImage
  verbose_name = 'Изображение'
  verbose_name_plural = 'Изображения'
  max_num = 10
  extra = 0
  can_delete = True


class ProductAdmin(admin.ModelAdmin):
  inlines = [ProductImageInline,]


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


admin.site.register(Categories, CategoryFather)
