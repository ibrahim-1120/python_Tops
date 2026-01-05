from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',index,name='index'),
    path('cart',cart,name='cart'),
    path('contact',contact,name='contact'),
    path('blog',blog,name='blog'),
    path('home',home,name='home'),
    path('registration',registration,name='registration'),
    path('logout',user_logout,name='logout')
]