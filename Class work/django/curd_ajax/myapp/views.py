from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='post':
        data = request.post
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        print(name,email,phone)
        students.objects.create(name=name,email=email,phone=phone)

        return HttpResponse("Registration successfully")
        