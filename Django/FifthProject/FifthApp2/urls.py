from django.urls import path

from FifthApp2 import views

urlpatterns=[
    path('generate',views.generate_fun),
    path('read_data', views.read_data_fun)

]