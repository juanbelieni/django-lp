from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404


# Create your views here.


def index(request):
    return HttpResponse("<h1>TELEGRAM2.apk baixar</h1>")

def introducao(request):
    return render(request, 'telegram2/introducao.html')

def post(request, text):
    if text=="abacaxi" or text=="morango":
        return HttpResponse(f"<b>Gosto de {text}<b\>")
    
    if text=="melancia" or text=="cereja":
        return HttpResponse(f"<b>Não gosto de {text}<b\>")
    else:
        raise Http404()
        
def redireciona_inicio(request):
    url = reverse("introducao")
    return HttpResponseRedirect(url)

def visualizacao(request):
    
    filmes = ["A Origem", "Inferno", "Pearl Harbor", "Forest Gump"]
    context = {
        "nome": "Pedro",
        "idade": 18,
        "ocupacao": "desempregado",
        "filmes": filmes
    }
    return render(request, 'telegram2/visualizacao.html', context)
    