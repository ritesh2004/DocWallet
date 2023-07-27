from django.shortcuts import render

from .models import Details
from .serializers import Detailserializer

from rest_framework import viewsets

# Create your views here.
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import Userserializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def signin(request):
    user = get_object_or_404(User,username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail":"Not found"},status=status.HTTP_404_NOT_FOUND)
    
    token,created = Token.objects.get_or_create(user=user)
    serializer = Userserializer(instance=user)
    return Response({"token":token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = Userserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_token(request):
    # serializer = Userserializer(instance=request.data['username'])
    return Response(f"passed for {request.user.email}")


class DetailViewSet(viewsets.ViewSet):
    def retrieve(self,request,username):
        queryset = Details.objects.all()
        userDet = get_object_or_404(queryset,username=username)
        serializer = Detailserializer(userDet)
        # print(serializer.data)
        return Response(serializer.data)
