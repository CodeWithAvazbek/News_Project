from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, News
from .forms import ContactForm


def index(request):
    all_news = News.objects.all().order_by('-publish_time')
    context = {
        'all_news': all_news[:5]
    }
    return render(request, 'index.html',context=context)


def news_list(request):
    news = News.objects.filter(status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_list.html', context=context)


def detail(request, news_id):
    new = get_object_or_404(News, id=news_id)
    return render(request, 'news/detail.html', {'new': new})


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse('Xabaringiz jo\'natilti')
    return render(request, 'pages/contact.html', {})


def page_404(request):
    return render(request, 'pages/404.html', {})


