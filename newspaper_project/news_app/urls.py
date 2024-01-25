from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('economics/', views.economics, name='economics'),
    path('worldnews/', views.worldnews, name='worldnews'),
    path('sports/', views.sports, name='sports'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('contact/', views.contact, name='contact'),
]
