# Generated by Django 4.0.5 on 2022-06-30 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_choice_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
