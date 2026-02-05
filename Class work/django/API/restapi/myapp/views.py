from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_api(request):
    return Response('get api calling')

@api_view(['POST'])
def post_api(request):
    return Response('post api calling')

@api_view(['PUT'])
def put_api(request):
    return Response('put api calling')

@api_view(['Delete'])
def delete_api(request):
    return Response('delete api calling')