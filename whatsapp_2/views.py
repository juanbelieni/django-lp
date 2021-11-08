from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    return HttpResponse("<h1> Eu odeio tudo </h1>")

def contacts(request):
    return render(request, 'whatsapp_2/contacts.html')

def profile(request, param):
    return HttpResponse(f"<h1> Nome: {param} <h2>")

def redirect_to_contacts(request):
    url = reverse("contacts")
    return HttpResponseRedirect(url)

def secret(request):
    context = {
        "name": "Tio Rafa",
        "beloved": "Cowboy Bebop"
    }
    return render(request, 'whatsapp_2/secret.html', context)