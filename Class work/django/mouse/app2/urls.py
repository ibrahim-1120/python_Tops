from django.urls import path
from app2.views import*

urlpatterns=[
    path('',index,name='index'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('help',help,name='help')
]