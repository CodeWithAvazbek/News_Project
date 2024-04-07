from django.shortcuts import render, get_object_or_404
from .models import Category, News


def index(request):
    return render(request, 'index.html')


def news_list(request):
    news = News.objects.filter(status=News.Status.Published)
    # news = News.published.all()
    context = {
        'news': news
    }
    return render(request, 'news/news_list.html', context=context)


def detail(request, news_id):
    new = get_object_or_404(News, id=news_id)
    return render(request, 'news/detail.html', {'new': new})



