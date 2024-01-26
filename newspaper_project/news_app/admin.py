from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'created_at')
    list_filter = ('category', 'author')

admin.site.register(Article, ArticleAdmin)
