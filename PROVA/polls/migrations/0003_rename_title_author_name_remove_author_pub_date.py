# Generated by Django 4.0.5 on 2022-06-03 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='pub_date',
        ),
    ]
