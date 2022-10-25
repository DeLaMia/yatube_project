from re import template
from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request,slug):
    template='posts/group_list.html'
    text="Здесь будет информация о группах проекта Yatube"
    context={
        'text':text
    }    
    return render(request, template, context)


