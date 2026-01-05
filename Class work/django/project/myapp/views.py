from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import JsonResponse,HttpResponse

# Create your views here.


def index(request):
    return render(request,'index.html')


def cart(request):
    return render(request,'cart.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')


def registration(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request,'registration.html',{'err':'Username already exits !'})
        else:
            u = User(first_name=fname,last_name=lname,username=username)
            u.set_password(password)
            u.save()
            return render(request,'register.html',{'msg':'Registration done sucessfully !'})
    return render(request,'registration.html')

def home(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        u=authenticate(username=username,password=password)

        if u is None:
            return render(request,'index.html',{'err':'invalid details'})
        else:
            login(request,u)
            return redirect('index')
        
    return render(request,'home.html')

def user_logout(request):
    logout(request)
    return render(request,'home.html')