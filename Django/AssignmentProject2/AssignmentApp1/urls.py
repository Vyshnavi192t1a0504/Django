from django.urls import path

from AssignmentApp1 import views

urlpatterns = [
    path('big',views.big_fun),
    path('palindrome',views.palindrome_fun)

    ]