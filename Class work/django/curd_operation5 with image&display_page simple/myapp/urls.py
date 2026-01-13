from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',index,name='index'),
    path('display',display,name='display'),
    path('reg',reg,name='reg'),
    path('delete',delete,name='delete'),
    path('edit',edit,name='edit')
]