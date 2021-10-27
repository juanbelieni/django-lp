from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1>TELEGRAM2.apk baixar</h1>")

def introducao(request):
    return render(request, 'telegram2/introducao.html')
