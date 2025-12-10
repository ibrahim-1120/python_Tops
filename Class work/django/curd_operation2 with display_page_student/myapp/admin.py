from django.contrib import admin
from myapp.models import *
# Register your models here.

class show(admin.ModelAdmin):
    list_display=('name','email','age','phone')

admin.site.register(student,show)
