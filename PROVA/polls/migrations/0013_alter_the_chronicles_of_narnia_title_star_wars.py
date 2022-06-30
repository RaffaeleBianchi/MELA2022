# Generated by Django 4.0.5 on 2022-06-27 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_the_chronicles_of_narnia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='the_chronicles_of_narnia',
            name='Title',
            field=models.CharField(max_length=40),
        ),
        migrations.CreateModel(
            name='Star_Wars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=60)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.author')),
            ],
        ),
    ]