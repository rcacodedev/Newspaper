from django.shortcuts import render

def index(request):
    return render(request, 'news_app/index.html')

def economics(request):
    return render(request, 'news_app/economics.html')

def worldnews(request):
    return render(request, 'news_app/worldnews.html')

def sports(request):
    return render(request, 'news_app/sports.html')

def entertainment(request):
    return render(request, 'news_app/entertainment.html')

def contact(request):
    return render(request, 'news_app/contact.html')