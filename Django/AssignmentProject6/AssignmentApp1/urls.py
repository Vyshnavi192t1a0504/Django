from django.urls import path

from AssignmentApp1 import views

urlpatterns=[
    path('',views.index_fun),#it will display addcar.html file
    path('addmobile',views.addmobile_fun), # inside this function write a code to insert a record in car table
    path('display',views.display_fun),
    path('display', views.display_fun, name='display'),
    path('update/<int:id>', views.update_fun, name='update'),
    path('del/<int:id>', views.del_fun, name='del')

]