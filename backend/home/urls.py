from django.contrib import admin
from django.urls import path,include
from .views import signin,signup,get_token

from .views import DetailViewSet

urlpatterns = [
    path('signin/', signin, name="signin"),
    path('signup/', signup, name="signup"),
    path('token/', get_token, name="token"),
    path('details/<username>/', DetailViewSet.as_view({'get':'retrieve'}))
]