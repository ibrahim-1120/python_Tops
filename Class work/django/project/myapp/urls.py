from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',index,name='index'),
    path('about',about,name='about'),
    path('booking',booking,name='booking'),
    path('conatct',contact,name='contact'),
    path('menu',menu,name='menu'),
    path('service',service,name='service'),
    path('team',team,name='team'),
    path('testimonial',testimonial,name='testimonial'),
    path('login',login,name='login'),
    path('registration',registration,name='registration'),
    path('table',table,name='table'),

    path('user_login',user_login,name='user_login'),
    path('user_registration',user_registration,name='user_registration'),
    path('user_logout',user_logout,name='user_logout')
]