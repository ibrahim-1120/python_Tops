from rest_framework import serializers
from curdapp.models import *

class studentser(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

