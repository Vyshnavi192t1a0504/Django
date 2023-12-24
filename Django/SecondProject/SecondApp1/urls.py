from django.urls import path

from SecondApp1 import views

urlpatterns =[
    path('home',views.home_fun)
]