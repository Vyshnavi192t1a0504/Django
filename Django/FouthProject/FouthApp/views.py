from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_fun(request):
    return render(request, 'addition.html')


def readdata_fun(request):
    num1 = int(request.POST['txtNum1'])
    num2 = int(request.POST['txtNum2'])
    result = num1 + num2
    data={
        'Sum':result,
        'num1':num1,
        'num2':num2
    }
    return render(request,'Addition.html',data)

