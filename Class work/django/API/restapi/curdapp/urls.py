from django.urls import path
from curdapp.views import *

urlpatterns=[
    path('view',view_student,name='view'),
    path('add',add_student,name='add')
]