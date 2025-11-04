from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def orders(request):
    return HttpResponse("ALL Orders")


def order(request, order_id):
    a = request.GET.values()
    print(list(a))
    print(request.GET)
    user = request.auser()
    print('user', user)
    return HttpResponse(f"Order {order_id} ")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
