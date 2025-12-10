from django.contrib import admin
from myapp.models import *

class empdis(admin.ModelAdmin):
    list_display = ('ename','email','age','salary','department')


admin.site.register(emp,empdis)

# Register your models here.


