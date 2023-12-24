from django.shortcuts import render


# Create your views here.
def generate_fun(request):
    return render(request, 'generate.html')


def read_data_fun(request):
    n1 = int(request.POST['txtNum1'])
    n2 = int(request.POST['txtNum2'])
    if n1 < n2:
        x = list(range(n1, n2 + 1))
        return render(request, 'Result2.html', {'data': x})
    else:
        return render(request, 'generate.html', {'msg': 'num1 value should be less than num2'})
