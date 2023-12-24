from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return render(request,'index.html')


def readdata_fun(request):
    n1 = int(request.POST['txtN1'])
    n2 = int(request.POST['txtN2'])
    x=list(range(n1,n2+1))
    return render(request,'result.html',{'data':x})