from django.contrib import admin
from myApp.models import *


class studentdata(admin.ModelAdmin):
    list_display=('first_name','last_name','email')

# class coursedata(admin.ModelAdmin):
#     list_display=('title','disctription')
# Register your models here.

admin.site.register(student,studentdata)
admin.site.register(course,)
