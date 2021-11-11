from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse('<h1>IG2</h1>')
    
def perfil(request):
    return render(request, "instagram2/index.html")

def profile(request, param):
    if param == "@TioR4fa":
        lista_de_gostos = ["Cowboy Bebop", "Cavaleiros do Zodiaco", "python", "engenharia"]
        pfp = "Imagem do dedão"
        user = param
        nome = "Tio Rafa"
        bio = "O monte Everest está repleto de cadáveres de pessoas que um dia foram muito determinadas"

    elif param == "@morfeudoidao":
        lista_de_gostos = ["Jogos"]
        pfp = "Imagem minha"
        user = param
        nome = "Gustavo"
        bio = "Sou estudante de Ciência de dados"

    elif param == "@yuri":
        lista_de_gostos = ["SVD","FGV","AL", "Siglas"]
        pfp = "Imagem dele"
        user = param
        nome = "Yuri"
        bio = "Sou professor e coordenador de Ciência de Dados"

    context = {
        "perfil": param[1:],
        "pfp" : pfp,
        "name": nome,
        "user": user,
        "bio": bio,
        "gostos": lista_de_gostos
    }

    return render(request, f'instagram2/template.html', context)

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
