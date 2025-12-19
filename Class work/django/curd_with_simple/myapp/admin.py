from django.contrib import admin
from myapp.models import student

# Register your models here.


class data(admin.ModelAdmin):
    list_display=('name','email','age')


admin.site.register(student,data)