# Generated by Django 4.1.4 on 2023-01-07 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]
