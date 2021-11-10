from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


def index(request):
    return render(request, "app_django/index.html")

def facul(request):
    context = {
        "status":"atrasado",
    }
    return render(request, 'app_django/faculdade.html', context)

def outros(request):
    compras = ["base","tênis","shorts","capinha celular", "bronzeador", "primer"]
    context = {
        "compras": compras, 
    }
    return render(request, "app_django/outros.html", context)

def redirect_faculdade(request):
    redirect_url = reverse("faculdade")
    return HttpResponseRedirect(redirect_url)

def by_day(request, day):
    if day < 1 or day > 7:
        return HttpResponseNotFound("<h1 style=color:red;text-align:center;>Você está enganado meu amigo, essa página não existe</h1>")
    elif day == 1: 
        return render(request, "app_django/domingo.html")
    elif day == 2: 
        return render(request, "app_django/segunda.html")
    elif day == 5: 
        return render(request, "app_django/quinta.html")
    elif day == 7: 
        return render(request, "app_django/sabado.html")
    else:
        return HttpResponse("<h1>Sem compromissos por aqui</h1>")