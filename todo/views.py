from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("<h1>TODO APP</h1>")

# Redirect to '/whatsapp2/'
def zapzap2(request):
    return HttpResponseRedirect('/whatsapp2')

# Return all todos
def todos(request):
    return render(request, "todo/index.html")


# Create dynamic view
def todo(request, id):
    return HttpResponse(f"<h1>TODO {id}</h1>")