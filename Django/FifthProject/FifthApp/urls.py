from django.urls import path

from FifthApp import views

urlpatterns=[
    path('',views.home_fun),
    path('readdata',views.readdata_fun)

]