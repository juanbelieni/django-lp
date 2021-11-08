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

# Create view with 'todo-2.html' template
def todo_2(request):
    data = { 'name': 'Mr. LinkedIn' }
    return render(request, "todo/todo-2.html", data)

def animes(request):
    animes = [
        'Neon Genesis Evangelion',
        'Cowboy Bebop',
        'Death Note',
        'Full Metal Alchemist',
    ]
    return render(request, "todo/filtros.html", { 'animes': animes })