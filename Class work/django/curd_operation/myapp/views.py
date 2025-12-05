from django.shortcuts import render
from myapp.models import*

# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    name= request.POST.get('name')
    email= request.POST.get('email')
    age= request.POST.get('age')

  
    student.objects.create(name=name, email=email, age =age)
    return render(request,'index.html',{'message':'student register sucessfull'})
