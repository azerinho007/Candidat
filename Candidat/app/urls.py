from django.contrib import admin
from django.urls import path
from .views import api, UserUpdateView,stat,filter

app_name = "app"
urlpatterns = [
    path('update/<int:pk>/',UserUpdateView.as_view(),name='update'),
    path('api/<int:pk>',api,name="api"),
    path('stat/<int:pk>',stat,name='stat'),
    path('filter/<str:url>',filter),
]