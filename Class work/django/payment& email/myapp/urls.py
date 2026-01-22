from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',email,name='email'),
    path('payment',payment,name='payment'),
    path('pay',pay,name='pay')
]