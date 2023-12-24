from django.shortcuts import render


# Create your views here.
def even_fun(request):
    return render(request, 'EvenOdd.html')


def readdata_fun(request):
    num = int(request.POST['txtNum'])
    return render(request, "Result1.html", {'data':num})
