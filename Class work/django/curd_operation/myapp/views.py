from django.shortcuts import render,redirect
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


def display(request):
    students = student.objects.all()
    return render(request,'display.html',{'students':students})


def delete(request):
    id= request.GET.get("id")
    st = student.objects.get(pk=id)
    st.delete()
    return redirect("display")