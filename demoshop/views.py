from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import Banner,  CreditInfo, Categories, SubCategory, CreditProgram, ContactInfo, Products, \
    ProductImage
import random


@never_cache
def index(request):
    banners = Banner.objects.order_by('id')
    credit = CreditInfo.objects.order_by('id')
    credit_programm = CreditProgram.objects.order_by('id')
    categories = Categories.objects.order_by('id')
    nums = [random.randint(0, 1000) for _ in range(100)]
    sub_cat = SubCategory.objects.order_by('id')
    contact = ContactInfo.objects.order_by('id')
    products = Products.objects.order_by('id')
    product_images = ProductImage.objects.order_by('id')
    context = {'title': 'Главная страница',
               'banners': banners,
               'credit': credit,
               'program': credit_programm,
               'nums': nums,
               'categories': categories,
               'subcat': sub_cat,
               'contact': contact,
               'products': products,
               'product_images': product_images,
               }
    return render(request, "demoshop/index.html", context=context)
