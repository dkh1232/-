from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index',views.index),
    path('regist',views.register),
    path('login',views.login),
    path('logout',views.logout),
]