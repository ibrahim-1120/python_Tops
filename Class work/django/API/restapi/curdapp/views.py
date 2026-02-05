from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from curdapp.models import *
from curdapp.serializer import *
# Create your views here.

@api_view(['GET'])
def view_student(request):                         

    students = student.objects.all()                         
    ser =studentser(students,many=True)                         
    return Response({'data':ser.data})                         

@api_view(['POST'])
def add_student(request):
    stdata = request.data
    ser =studentser(data=stdata) 
    if not ser.is_valid():
        return Response({"errors":ser.error,"message":"something went wrong"})
    else:
        ser.save()
        return Response({'data':ser.data,'message':'data is inserted'})