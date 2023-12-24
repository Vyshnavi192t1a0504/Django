from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_fun(request):
    return HttpResponse("hi welcome to django app")
