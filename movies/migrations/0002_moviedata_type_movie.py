# Generated by Django 3.1.1 on 2023-04-02 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='type_movie',
            field=models.CharField(default='action', max_length=100),
        ),
    ]
