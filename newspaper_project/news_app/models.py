from django.db import models

CHOICES = (
    ('ECONOMICS', 'ECONOMICS'),
    ('WORLD NEWS', 'WORLD NEWS'),
    ('SPORTS', 'SPORTS'),
    ('ENTERTAINMENT', 'ENTERTAINMENT'),
    ('CONTACT', 'CONTACT'),
)

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=CHOICES)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return self.title