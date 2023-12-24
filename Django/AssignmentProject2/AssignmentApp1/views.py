from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def big_fun(request):
    a = 30
    b = 10
    c = 25
    greater = None
    if a > b:
        if a > c:
            greater = a
        else:
            greater = c
    else:
        if b > c:
            greater = b
        else:
            greater = c
    return HttpResponse(f"biggest of 3 numbers is : {greater}")


def palindrome_fun(request):
    str = "malayalam"
    revstr = ""
    for i in str:
        revstr = i + revstr
    if str == revstr:
        return HttpResponse("the string is a palindrome")
    else:
        return HttpResponse("the string is not a palindrome")
