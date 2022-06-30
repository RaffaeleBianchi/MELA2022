# Generated by Django 4.0.5 on 2022-06-27 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_rename_fantasy_harry_potter'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='The_lord_of_rings',
            new_name='The_Chronicles_of_Narnia',
        ),
        migrations.CreateModel(
            name='The_lord_of_ring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=40)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.author')),
            ],
        ),
    ]