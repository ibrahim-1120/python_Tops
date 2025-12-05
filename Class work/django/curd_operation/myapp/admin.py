from django.contrib import admin
from myapp.models import *

class studentdata(admin.ModelAdmin):
    list_display=('name','age','email')
    

# Register your models here.

admin.site.register(student,studentdata)