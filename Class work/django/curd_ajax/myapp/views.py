from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='post':
        data = request.post
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        