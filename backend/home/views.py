from django.shortcuts import render
from django.http import JsonResponse

from .models import Details,AadhaarDetails,PANdetails,IssuedDoc
from .serializers import Detailserializer,AadhaarSerializer,PANSerializer,IssuedDocSerializer

from rest_framework import viewsets

from rest_framework.decorators import action

# Create your views here.
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from knox.models import AuthToken
from rest_framework.views import View

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
    
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user = user
        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])

def getView(request):
    routes = [
        "/token",
        "/token/refresh"
    ]
    return JsonResponse(routes, safe=False) 


class DetailViewSet(viewsets.ViewSet):
    def retrieve(self,request,username=None):
        queryset = Details.objects.all()
        userDet = get_object_or_404(queryset,username=username)
        serializer = Detailserializer(userDet)
        # print(serializer.data)
        return Response(serializer.data)
    
    

class DetailCreateViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = Detailserializer
    
    
class AadhaarViewSet(viewsets.ViewSet):
    def retrieve(self,request,aadhaarno=None):
        # print("Aadhaar no: ",aadhaarno)
        queryset = AadhaarDetails.objects.all()
        userDet = get_object_or_404(queryset,aadhar_no=aadhaarno)
        serializer = AadhaarSerializer(userDet)
        # print(serializer.data)
        return Response(serializer.data)
    
    
class PANViewSet(viewsets.ViewSet):
    def retrieve(self,request,panno=None):
        queryset = PANdetails.objects.all()
        userDet = get_object_or_404(queryset,pan_no=panno)
        serializer = PANSerializer(userDet)
        # print(serializer.data)
        return Response(serializer.data)
    
class IssuedDocViewSet(viewsets.ViewSet):
    def retrieve(self,request,cardname=None,username=None):
        queryset = IssuedDoc.objects.all()
        docs = get_object_or_404(queryset, category=cardname, username=username)
        serializer = IssuedDocSerializer(docs)
        
        return Response(serializer.data)
    
class IssuedDocCreateViewset(viewsets.ModelViewSet):
    queryset = IssuedDoc.objects.all()
    serializer_class = IssuedDocSerializer
