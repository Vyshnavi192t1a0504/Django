from django.urls import path

from ThirdApp import views

urlpatterns=[
    path('',views.index_fun), # it will display index.html page
    path('readdata',views.readdata_fun)
]