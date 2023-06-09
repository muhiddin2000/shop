from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from category.models import Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from products.models import Product
from .models import Order, OrderItem


# Create your views here.
def registerpage(request):
    til = request.LANGUAGE_CODE
    if request.user.is_authenticated:
        return redirect(f'/{til}')

    if request.method == "POST":
        username = request.POST['username']
        pas1 = request.POST['pas1']
        pas2 = request.POST['pas2']
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username already exists")
            return redirect(f"/{til}/register")

        if pas1 != pas2:
            messages.error(request, "Passwords doesnt match!")
            return redirect(f"/{til}/register")
        else:
            User.objects.create_user(username=username, password=pas1)
            return redirect(f'/{til}')

    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'register.html', context=context)


def loginpage(request):
    til = request.LANGUAGE_CODE

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pas1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'/{til}')
        else:
            messages.error(request, "Username or Password wrong!!")
            return redirect(f"/{til}/login")
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('home')


def orders(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=request.user)
        orders = order.orderitem_set.all()
        items = orders
        all_summa = order.all_summa
        item_count = order.item_count

    else:
        items = [],
        all_summa = 0
        item_count = 0
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
        "all_summa": all_summa,
        'item_count': item_count
    }
    return render(request, 'orders.html', context=context)


def update(request):
    import json
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=user)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)
    orderitem.save()
    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse('Mahsulot qoshildi', safe=False)
