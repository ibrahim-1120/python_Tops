from django.shortcuts import render

# Create your views here.

def email(request):
    return render(request,'email.html')