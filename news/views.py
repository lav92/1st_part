from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def index(request):
    all_news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'news': all_news,
        'title': 'News',
        'categories': categories,
    }
    return render(request, 'news/index.html', context)


def category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category,
    }
    return render(request, 'news/category.html', context=context)
