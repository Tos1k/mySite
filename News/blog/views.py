from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render

from blog.models import *

menu = ["О Сайте", "Добавить статью", "Обратная связь", "Войти"]


def show_category(request,cat_id):
    return HttpResponse(f"Отображение категории с id = {cat_id}")


def index(request, cat_id):  # HttpRequest
    posts = Post.objects.all()
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }

    return render(request, "blog/index.html", context=context)


def about(request):  # HttpRequest
    return render(request, "blog/about.html", {'title': 'О нас'})


def categories(request, cat):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1> Архив по годам </h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
