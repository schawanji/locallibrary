# Generated by Django 4.0.8 on 2023-05-16 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_userprofile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
