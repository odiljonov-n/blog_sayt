from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logaut
def index_view(request):
    active_category = Category.objects.get(is_active=True)
    context = {
        'banner': Banner.objects.all().order_by('-id')[:2],
        'about': About.objects.last(),
        'services': Servise.objects.all().order_by('-id')[:3],
        'r_pizza_meal': Meal.objects.all().order_by('-id')[:3],
        'l_pizza_meal': Meal.objects.all().order_by('-id')[3:6],
        'menu': Meal.objects.all().order_by('-id')[6:15],
        'client': Client.objects.all().order_by('-id')[:4],
        'blog': Blog.objects.all().order_by('-id')[:3],
        'info': Info.objects.last(),
        'active_meal': Meal.objects.filter(category=active_category).order_by('-id')[:3]
    }
    return render(request, 'index.html', context)



def filter_meal_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'banner': Banner.objects.all().order_by('-id')[:2],
        'about': About.objects.last(),
        'services': Servise.objects.all().order_by('-id')[:3],
        'r_pizza_meal': Meal.objects.all().order_by('-id')[:3],
        'l_pizza_meal': Meal.objects.all().order_by('-id')[3:6],
        'left_menu': Meal.objects.all().order_by('-id')[6:10],
        'right_menu': Meal.objects.all().order_by('-id')[10:14],
        'menu': Meal.objects.all().order_by('-id')[6:15],
        'client': Client.objects.all().order_by('-id')[:4],
        'blog': Blog.objects.all().order_by('-id')[:3],
        'info': Info.objects.last(),
        'filter_meal': Meal.objects.filter(category=category),
    }
    return render(request, 'index.html', context)

def menu_view(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'r_pizza_meal': Meal.objects.all().order_by('-id')[:3],
        'l_pizza_meal': Meal.objects.all().order_by('-id')[3:6],
        'left_menu': Meal.objects.all().order_by('-id')[6:10],
        'right_menu': Meal.objects.all().order_by('-id')[10:14],
    }
    return render(request, 'menu.html',context)


def service_view(request):
    return render(request, 'services.html')

def blog_view(request):
    context = {
        'blogs': Blog.objects.all().order_by('-id')[:6]
    }
    return render(request, 'blog.html',context)

def blog_singe_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog': Blog,
        'blog': Blog_Category.objects.all().order_by('-id')[:6],
        'tags': Tag.objects.all().order_by('-id')[:8],
        'last_blogs': Blog.objects.all().order_by('-id')[:3]

    }
    return render(request, 'blog-single.html', context)



def login_view(request):
    return render(request, 'login.html')



def regisgter_view(request):
    if request.method == "POST":
        username = request.POST['username']
        passwort = request.POST['passwort']
        User.objects.create_user(
            username=username,
            passwort=passwort
        )
    return redirect('index_url')
    return render(request, 'register.html')




