from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1> Eu odeio tudo </h1>")


def elogio(request):
    return render(request, 'appCleomar/elogio.html')


def todo(request, id):
    return HttpResponse(f"<h1>TODO {h1}</h1>")