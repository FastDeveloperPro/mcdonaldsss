from django.shortcuts import render
from .models import Deals, Post, Drinks, Foods



def index(request):
    foods = Foods.objects.all().order_by()[:10]
    deals = Deals.objects.all().order_by()[:10]
    drinks = Drinks.objects.all().order_by()[:10]#firs 7 products
    post = Post.objects.all().order_by()[:3]
    page = "home"
    context = {
        'page':page,
        'deals': deals,
        'foods': foods,
        'drinks': drinks,

    }
    return render(request, 'index.html', context)


def foods(request):
    foods = Foods.objects.all().order_by()[:10]
    return render(request, 'foods.html', {'foods':foods})

def drinks(request):
    drinks = Drinks.objects.all().order_by()[:10]
    return render(request, 'drinks.html', {'drinks':drinks})


def deals(request):
    deals = Deals.objects.all().order_by()[:10]
    return render(request, 'deals.html', {'deals':deals})


def trending_now(request):
    context = {
    }
    return render(request, 'trending.html',context)


def about(request):
    context = {
    }
    return render(request, 'about.html',context)


def locate(request):
    context = {
    }
    return render(request, 'location.html',context)