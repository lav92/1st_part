from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm


def index(request):
    all_news = News.objects.order_by('-created_at')
    context = {
        'news': all_news,
        'title': 'News',
    }
    return render(request, 'news/index.html', context)


def category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context=context)


def view_news(request, news_id):
    item_news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news': item_news})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', context={'form': form})
