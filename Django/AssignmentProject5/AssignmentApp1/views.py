from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return render(request,'index.html')


def readdata_fun(request):
    n1 = int(request.POST['txtN1'])
    n2 = int(request.POST['txtN2'])
    operation = request.POST['txtoperation']
    result = 0
    if operation == 'add':
        result = n1 + n2
    elif operation== 'sub':
        result = n1 - n2
    elif operation == 'mul':
        result = n1 * n2
    elif operation == 'div':
        if n1 > n2:
            result = n1 / n2
        else:
            result = f"{n1} is greater than {n2}"

    elif operation == 'rem':
        if n1 > n2:
            result = n1 % n2
        else:
            result = f"{n1} is greater than {n2}"
    return render(request,'index.html',{'data':result})