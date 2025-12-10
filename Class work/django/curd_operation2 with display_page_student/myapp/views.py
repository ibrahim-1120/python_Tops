from django.shortcuts import render,redirect
from myapp.models import student

# Create your views here.

def index(request):
    return render (request,'index.html')



def register(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    phone = request.POST.get('phone')

    if not id:
        student.objects.create(name=name, email=email, age=age, phone=phone)
        return render (request,'index.html',{'sucess':'student register sucessfully'})

    else:
        st= student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.age=age
        st.phone=phone
        st.save()
        return render(request,'index.html',{'sucess':'student updated sucessfully'})
    

def display(request):
    students= student.objects.all()
    return render(request,'display.html',{'students':students})

def delete(request):
    id= request.GET.get("id")
    st = student.objects.get(pk=id)
    st.delete()
    return redirect ("display")


def edit(request):
    id = request.GET.get('id')
    st=student.objects.get(pk=id)
    return render(request,'index.html',{'st':st})
    