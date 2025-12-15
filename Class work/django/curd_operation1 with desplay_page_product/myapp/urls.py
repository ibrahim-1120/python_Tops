from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",index,name='index'),
    path('display',display,name='display'),
    path('register',register,name='register'),
    path('edit',edit,name='edit'),
    path('delete',delete,name='delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)