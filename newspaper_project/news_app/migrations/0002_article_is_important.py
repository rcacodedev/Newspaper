# Generated by Django 5.0.1 on 2024-01-26 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_important',
            field=models.BooleanField(default=False),
        ),
    ]
