from rest_framework import serializers
from .models import *

class TableAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableAll
        # fields = ('id','title','detail') # '__all__' เลือกทั้งหมด
        fields =  '__all__' 
        