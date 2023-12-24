from django.http import HttpResponse


def prime_fun(request):
    prime = []
    for i in range(2, 100):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            prime.append(i)
    return HttpResponse(f"Prime numbers {prime}")


def even_fun(request):
    even = []
    for i in range(1,100):
        if i % 2 == 0:
            even.append(i)
    return HttpResponse(f"Even numbers {even}")

