from django.urls import path
from myapp.views import *

urlpatterns=[
    path("get_api",get_api,name="get_api")
]