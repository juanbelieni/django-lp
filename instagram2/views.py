from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse('<h1>IG2</h1>')
    
def perfil(request):
    return render(request, "instagram2/index.html")

def profile(request, param):
    return HttpResponse(f"<h1> Nome: {param} <h2>")

def redirect_to_perfil(request):
    url = reverse("perfil")
    return HttpResponseRedirect(url)

def tiorafa(request):
    lista_de_gostos = ["Cowboy Bebop", "Cavaleiros do Zodiaco", "python", "engenharia"]

    context = {
        "pfp" : "Imagem do dedão",
        "name": "Tio Rafa",
        "user": "@TioR4fa",
        "beloved": "Cowboy Bebop",
        "gostos": lista_de_gostos
    }
    return render(request, 'instagram2/tioRafa.html', context)
