# Generated by Django 4.2.6 on 2023-11-20 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='picture',
        ),
    ]