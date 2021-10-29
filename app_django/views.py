from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Um belo exemplo</h1>")

def app_index(request):
    return render(request, 'app_django/app_index.html')