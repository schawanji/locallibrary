# Generated by Django 4.1.5 on 2023-04-22 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_author_book_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]
