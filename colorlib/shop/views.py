from django.shortcuts import render
from shop.models import Category
from shop.models import Product
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def allprodcat(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c=Category.objects.get(slug=p)
    product=Product.objects.filter(category__slug=p)
    return render(request,'product.html',{'product':product,'c':c})

def prodetail(request,p):
    p=Product.objects.get(slug=p)
    return render(request,'detail.html',{'p':p})

def register(request):
        if (request.method == "POST"):
            u = request.POST['u']
            p = request.POST['p']
            c = request.POST['c']
            e = request.POST['e']
            f = request.POST['f']
            l = request.POST['l']
            if (p == c):
                u = User.objects.create_user(username=u,
                                             password=p,
                                             email=e,
                                             first_name=f,
                                             last_name=l)
                u.save()
                return user_login(request)

        return render(request, 'register.html')


def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return allprodcat(request)
        else:
            messages.error(request, "Invalid User Credentials")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return allprodcat(request)
