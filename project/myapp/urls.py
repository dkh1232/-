from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('showlist/',views.showlist1),
    path('upfile/',views.upfile),
    path('savefile/',views.savefile),
    path('download/',views.download),
    # re_path(r'^savefile/$', views.savefile),
    # re_path(r'^download/$', views.download),
]