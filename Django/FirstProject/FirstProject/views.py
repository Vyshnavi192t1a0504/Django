from django.http import HttpResponse


def home_fun(request):
    return HttpResponse("hi welcome to django project")


def add_fun(request):
    a = 10
    b = 8
    sum = a+b
    return HttpResponse(f"sum of 2 numbers {sum}")