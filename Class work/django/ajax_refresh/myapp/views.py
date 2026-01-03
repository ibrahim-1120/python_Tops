
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def view(request):
    data = request.GET['data']
    row = ""
    if data=='sports':
        row+="<ul><li>Ball</li><li>Bat</li></ul>"
    elif data=='electric':
        row+="<ul><li>Fan</li><li>TV</li></ul>"
    elif data=='cosmetic':
        row+="<ul><li>lipstic</li><li>facewash</li></ul>"
    else:
        row+="No data found"

    return HttpResponse(row)


def view(request):
    data = request.GET['data']
    products = Product.objects.filter(name__startswith=data)
    return JsonResponse({"products":list(products.values())})

def countries(request):
    countries = Country.objects.all()
    return JsonResponse({"countries":list(countries.values())})

def states(request):
    cid = request.GET['cid']
    states = State.objects.filter(country_id=cid)
    return JsonResponse({"states":list(states.values())})

def cities(request):
    sid = request.GET['sid']
    cities = City.objects.filter(state_id=sid)
    return JsonResponse({"cities":list(cities.values())})
