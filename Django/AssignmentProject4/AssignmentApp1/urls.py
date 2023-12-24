from django.urls import path

from AssignmentApp1 import views

urlpatterns = [
    path('',views.home_fun),
    path('readdata',views.readdata_fun)
]