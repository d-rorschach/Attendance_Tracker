from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('input/',views.input,name='input'),
    path('calender/',views.calender,name='calender'),
    path('stats/',views.stats,name='stats'),
    path('input/new_schedule/',views.new_schedule,name='new_schedule'),
    path('calender/store_attendance/',views.store_attendance,name='store_attendance'),
]
