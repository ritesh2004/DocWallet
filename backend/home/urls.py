from django.contrib import admin
from django.urls import path,include
# from .views import signin,signup,get_token

from .views import DetailViewSet,AadhaarViewSet,PANViewSet,IssuedDocViewSet,DetailCreateViewSet

from .views import MyTokenObtainPairView
from .views import RegisterAPI

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

route = routers.DefaultRouter()
route.register("",DetailCreateViewSet,basename='create details')

urlpatterns = [
    path('login/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/register/', RegisterAPI.as_view(), name='register'),
    path('issued/<cardname>/<username>/',IssuedDocViewSet.as_view({'get':'retrieve'})),
    path('details/<username>/', DetailViewSet.as_view({'get':'retrieve'})),
    path('details/', include(route.urls)),
    path('aadhaar/<aadhaarno>/',AadhaarViewSet.as_view({'get':'retrieve'})),
    path('pan/<panno>/',PANViewSet.as_view({'get':'retrieve'})),
]