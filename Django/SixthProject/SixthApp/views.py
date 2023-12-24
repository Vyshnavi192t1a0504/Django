from django.http import HttpResponse
from django.shortcuts import render, redirect

from SixthApp.models import CarData


# Create your views here.
def index_fun(request):
    return render(request,'addcar.html')


def addcar_fun(request):
    c1=CarData()
    c1.car_name=request.POST['txtCarName']
    c1.car_company=request.POST['txtCarCompany']
    c1.car_model = request.POST['txtCarModel']
    c1.car_price= int(request.POST['txtCarPrice'])
    c1.fuel_type=request.POST['ddlFuelType']
    c1.save()

    return render(request,'addcar.html',{'msg':'Inserted successfully'})


def display_fun(request):
    data=CarData.objects.all() # it will return list of objects
    return render(request,'displaydata.html',{'Car':data})


def update_fun(request,id):
    c1 = CarData.objects.get(id=id)
    if request.method=='POST':
        c1.car_name = request.POST['txtCarName']
        c1.car_company = request.POST['txtCarCompany']
        c1.car_model = request.POST['txtCarModel']
        c1.car_price = int(request.POST['txtCarPrice'])
        c1.fuel_type = request.POST['ddlFuelType']
        c1.save()
        return redirect('display')
    else:
        return render(request,'updatedata.html',{'data':c1})


def del_fun(request,id):
    c1=CarData.objects.get(id=id)
    c1.delete()
    return redirect('display')