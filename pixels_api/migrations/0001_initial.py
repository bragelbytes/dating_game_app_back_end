# Generated by Django 3.2.6 on 2021-08-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('image', models.URLField()),
                ('genre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=1000)),
                ('image', models.URLField(blank=True)),
                ('name', models.CharField(max_length=32,blank=True)),
                ('age', models.CharField(max_length=32,blank=True)),
                ('fav_console', models.CharField(max_length=32,blank=True)),
                ('fav_games', models.ManyToManyField(to='pixels_api.Games',blank=True)),
            ],
        ),
    ]
