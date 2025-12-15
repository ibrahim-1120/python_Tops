from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')

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