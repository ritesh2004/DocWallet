from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Details,PANdetails,AadhaarDetails,IssuedDoc

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')    


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
        
class Detailserializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'
        
        
class AadhaarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AadhaarDetails
        fields = '__all__'
        
        
class PANSerializer(serializers.ModelSerializer):
    class Meta:
        model = PANdetails
        fields = '__all__'
        
class IssuedDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedDoc
        fields = '__all__'