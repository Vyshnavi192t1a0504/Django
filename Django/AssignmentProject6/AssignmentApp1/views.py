from django.shortcuts import render, redirect

from AssignmentApp1.models import MobileData


# Create your views here.
def index_fun(request):
    return render(request,'addmobile.html')


def addmobile_fun(request):
    m1 = MobileData()
    m1.mobile_name = request.POST['txtMobileName']
    m1.no_of_cameras =int( request.POST['txtNo_of_Cameras'])
    m1.mobile_ram = request.POST['txtMobileRam']
    m1.mobile_price = int(request.POST['txtMobilePrice'])
    m1.mobile_color= request.POST['txtMobileColor']
    m1.save()

    return render(request,'addmobile.html',{'msg':'Inserted Successfully'})


def display_fun(request):
    data = MobileData.objects.all()  # it will return list of objects
    return render(request, 'display.html', {'Mobile': data})


def update_fun(request,id):
    m1= MobileData.objects.get(id=id)
    if request.method == 'POST':
        m1.mobile_name = request.POST['txtMobileName']
        m1.no_of_cameras = int(request.POST['txtNo_of_Cameras'])
        m1.mobile_ram = request.POST['txtMobileRam']
        m1.mobile_price = int(request.POST['txtMobilePrice'])
        m1.mobile_color = request.POST['txtMobileColor']
        m1.save()
        return redirect('display')
    else:
        return render(request, 'update.html', {'data': m1})


def del_fun(request,id):
    c1 = MobileData.objects.get(id=id)
    c1.delete()
    return redirect('display')