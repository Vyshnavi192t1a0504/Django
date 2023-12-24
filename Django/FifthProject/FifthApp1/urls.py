from django.urls import path

from FifthApp1 import views

urlpatterns = [
    path('even',views.even_fun), #it will display evenodd.html page
    path('readdata',views.readdata_fun) #it will read the data and send to result1.html file
    ]