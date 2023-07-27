from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Details

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email')
        
class Detailserializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'