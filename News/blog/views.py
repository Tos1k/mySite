from django.http import HttpResponse,HttpResponseNotFound, Http404
from django.shortcuts import redirect


def index(request): #HttpRequest
    if (request.GET):
        print(request.GET)
    return HttpResponse("Домашняя страница")

def categories (request, cat):
    print (request.GET)
    return HttpResponse (f"<h1>Статьи по категориям<h1><p>{cat}</p>")

def archive(request, year):
    if int(year)>2022:
        raise redirect('home',permanent=True)
    return HttpResponse(f'<h1> Архив по годам </h1><p>{year}</p>')

def page_not_found (request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')