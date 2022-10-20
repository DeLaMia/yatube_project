from re import template
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):
    template='posts/index.html'    
    return render(request, template) 

def group_posts(request,slug):
    return HttpResponse('gryppa')


