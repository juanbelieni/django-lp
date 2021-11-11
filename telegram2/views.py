from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    return HttpResponse("<h1>TELEGRAM2.apk baixar</h1>")

def introducao(request):
    return render(request, 'telegram2/introducao.html')

def post(request, text):
    return HttpResponse(f"<b> Publicação: {text} <\b>")

def redireciona_inicio(request):
    url = reverse("introducao")
    return HttpResponseRedirect(url)

def visualizacao(request):
    filmes = ["A Origem", "Inferno", "Pearl Harbor", "Forest Gump"]
    context = {
        "nome": "Pedro",
        "idade": 18,
        "ocupacao": "desempregado",
        "flmes favoritos": filmes
    }
    return render(request, 'telegram2/visualizacao.html', context)
    