from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')


# Create your views here.
