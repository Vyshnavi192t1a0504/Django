from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_fun(request):
    return render(request, 'index.html')
    """
    rendor is used to redirected  html file
    request is your HTTP object
    index.html is html file 
    """


def readdata_fun(request):
    # write a code to read text box data
    name= request.POST['txtName']
    age= request.POST['txtAge']
    email = request.POST['txtMail']
    return HttpResponse(f"Name={name} , Age={age} , Email={email}")
