from django.shortcuts import render
from myapp.models import student

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    email=request.POST.get('email')
    age=request.POST.get('age')
    photo =request.FILES['photo']
    if not id:
        student.objects.create(name=name, email=email, age=age,photo=photo)
        return render (request,'index.html')

    else:
        st= student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.age=age
        st.save()
        return render(request,'index.html')
    
def display(request):
    students= student.objects.all()
    return render(request,'display.html',{'students':students})
