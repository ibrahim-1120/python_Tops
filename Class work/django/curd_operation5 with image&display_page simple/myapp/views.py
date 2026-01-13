from django.shortcuts import render,redirect
from myapp.models import simple

# Create your views here.

def index(request):

    return render(request,'index.html')

def display(request):
    simples = simple.objects.all()
    return render(request,'display.html',{'simples':simples})

def reg(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')

    if not id:
        simple.objects.create(name=name,email=email,phone=phone)
        return render(request,'index.html',{'msg':'Register done'})
    else:
        si=simple.objects.get(pk=id)
        si.name=name
        si.email=email
        si.phone=phone
        si.save()
        return render(request,'index.html',{'msg':'Data upated '})
    
def delete(request):
    id = request.GET.get("id")
    si = simple.objects.get(pk=id)
    si.delete()
    return redirect("display")

def edit(request):
    id = request.GET.get('id')
    si=simple.objects.get(pk=id)
    return render(request,'index.html',{'si':si})