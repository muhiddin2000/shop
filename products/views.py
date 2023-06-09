from django.shortcuts import render
from category.models import Category
from .models import Product

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 0df71028-6e79-11ed-a654-0242ac130002-0df710e6-6e79-11ed-a654-0242ac130002
# Create your views here.
def home(request):
    objects = Product.objects.all()
    products = Paginator(objects, 3)
    page_num = request.GET.get('page', 1)
    mahsulotlar = products.page(page_num)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'mahsulotlar': mahsulotlar,

    }

    return render(request, 'home.html', context=context)


def product_with_category(request, id):
    objects = Product.objects.filter(category=id)
    products = Paginator(objects, 1)
    page_num = request.GET.get('page', 1)
    mahsulotlar = products.page(page_num)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'mahsulotlar': mahsulotlar
    }

    return render(request, 'category_products.html', context=context)
