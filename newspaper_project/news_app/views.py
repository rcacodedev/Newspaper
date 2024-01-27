from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import Article
from .forms import CommentForm

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

class article_detail(View):
    def get(self, request, slug):
        article = Article.objects.get(slug=slug)

        context = {"article": article,
                   "comment_form": CommentForm(),
                   "comments": article.comments.all().order_by("-id"),}
        
        return render(request, "news_app/article_detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        article = Article.objects.get(slug=slug)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()

            return HttpResponseRedirect(reverse("article_detail", args=[slug]))
        
        
        context = {"article": article,
                   "comment_form": comment_form,
                   "comments": article.comments.all().order_by("-id"),
        }
        return render(request, "news_app/article_detail.html", context)