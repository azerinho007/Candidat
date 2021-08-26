from django.contrib import admin
from django.urls import path
from .views import signin,signup, home, verify,logout,UserUpdateView

app_name = "login"
urlpatterns = [
    path('',home, name="home"),
    path('signin/<int:msg>',signin, name="sign"),
    path('signup/',signup, name="sigp"),
    path('verify/<int:msg>',verify, name="verify"),
    path('logout/',logout,name="logout"),
]