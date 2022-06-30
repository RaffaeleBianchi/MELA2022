# Generated by Django 4.0.5 on 2022-06-03 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_title_author_name_remove_author_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fantasy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.author')),
            ],
        ),
    ]
