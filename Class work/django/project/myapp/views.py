from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

@login_required(login_url="login")
def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')

@login_required(login_url="login")
def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def table(request):
    return render(request,'table.html')

def user_registration(request):
    if request.method=='POST':
        data= request.POST
        uname = data.get('uname')
        email = data.get('email')
        password = data.get('pass')

        u=User(username=uname,email=email)
        u.set_password(password)
        u.save()
        return render(request,'registration.html',{'msg':'Registration successfully'})
    

def user_login(request):
    if request.method=='POST':
        data= request.POST
        uname = data.get('uname')
        password = data.get('pass')
        u= authenticate(username=uname,password=password)
        if u is not None:
            login(request,u)
            return redirect('index')
        else:
            return render('login',{'err':'Invalid details'})
        
def user_logout(request):
    logout(request)
    return redirect('login')
