from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import Banner, PromoBlock, CreditInfo, Categories
import random


@never_cache
def index(request):
    banners = Banner.objects.order_by('id')
    promo = PromoBlock.objects.order_by('id')
    credit = CreditInfo.objects.order_by('id')
    categories = Categories.objects.order_by('id')
    nums = [random.randint(0, 1000) for _ in range(100)]
    context = {'title': 'Главная страница',
               'banners': banners,
               'promo': promo,
               'credit': credit,
               'nums': nums,
               'categories': categories,
               }
    return render(request, "demoshop/index.html", context=context)