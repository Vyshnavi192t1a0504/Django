from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return render(request,'index.html')


def readdata_fun(request):
    name=request.POST['txtName']
    age=int(request.POST['txtAge'])
    email=request.POST['txtMail']
    sub1=int(request.POST['txtSub1'])
    sub2=int(request.POST['txtSub2'])
    sub3=int(request.POST['txtSub3'])
    avg=(sub1+sub2+sub3)//3
    data={'name':name,
          'age':age,
          'email':email,
          'avg':avg
          }

    return render(request,'result.html',data)