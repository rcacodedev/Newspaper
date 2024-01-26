from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    articles = Article.objects.all().order_by('-created_at')[:5]
    return render(request, 'news_app/index.html', {'articles': articles})

def economics(request):
    articles = Article.objects.filter(category='ECONOMICS')
    return render(request, 'news_app/economics.html', {'articles': articles})

def world_news(request):
    articles = Article.objects.filter(category='WORLD NEWS')
    return render(request, 'news_app/worldnews.html', {'articles': articles})

def sports(request):
    articles = Article.objects.filter(category='SPORTS')
    return render(request, 'news_app/sports.html', {'articles': articles})

def entertainment(request):
    articles = Article.objects.filter(category='ENTERTAINMENT')
    return render(request, 'news_app/entertainment.html', {'articles': articles})


def contact(request):
    articles = Article.objects.filter(category='CONTACT')
    return render(request, 'news_app/contact.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news_app/article_detail.html', {'article': article})