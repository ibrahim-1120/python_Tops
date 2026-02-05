from django.shortcuts import render
from myapp.views import *
from rest_framework.response import response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_api(request):
    return response('get api calling')