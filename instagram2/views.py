from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>IG2</h1>')
    
def perfil(request):
    return render(request, "intagram2/index.html")
