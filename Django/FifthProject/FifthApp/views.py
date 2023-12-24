from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return render(request,'Biggest.html')


def readdata_fun(request):
    num1 = int(request.POST['txtNum1'])
    num2 = int(request.POST['txtNum2'])
    #if num1>num2:
      #  biggest=num1
    #else:
      #  biggest=num2
    data={
        'num1':num1,
        'num2':num2
    }
    return render(request,'Result.html',data)



