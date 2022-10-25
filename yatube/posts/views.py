from re import template
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):
    template='posts/index.html'
    text="Это главная страница проекта Yatube"
    context={
        'text':text
    }        
    return render(request, template, context) 

def group_posts(request,slug):
    template='posts/group_list.html'
    text="Здесь будет информация о группах проекта Yatube"
    context={
        'text':text
    }    
    return render(request, template, context)


