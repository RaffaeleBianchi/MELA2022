# Generated by Django 4.0.5 on 2022-06-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_delete_choice_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]