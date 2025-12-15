from django.shortcuts import render,redirect
from myapp.models import product

# Create your views here.

def index(request):
    return render(request,"index.html")

def display(request):
    products = product.objects.all()
    return render(request,"display.html",{'products':products})

def register(request):
  id = request.POST.get('id')
  name = request.POST.get('name')
  cat = request.POST.get('cat')           
  price = request.POST.get('price')
  photo = request.FILES['photo']


  if not id:
     product.objects.create(name=name, cat=cat, price=price,photo=photo)
     return render(request,'index.html',{'sucess':'Product added sucessfully'})
  
  else:
     pt= product.objects.get(pk=id)
     pt.name=name
     pt.cat=cat
     pt.price=price
     pt.save()
     return render(request,'index.html',{'sucess':'Product updated sucessfully'})
  
def edit(request):
   id = request.GET.get('id')
   pt = product.objects.get(pk=id)
   return render(request,'index.html',{'pt':pt})
 
def delete(request):
   id =request.GET.get('id')
   pt = product.objects.get(pk=id)
   pt.delete()
   return redirect('display')