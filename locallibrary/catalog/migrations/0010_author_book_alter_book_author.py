# Generated by Django 4.1.5 on 2023-04-22 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_remove_book_language_book_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(related_name='authour', to='catalog.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='catalog.author'),
        ),
    ]
